import requests
import json
import boto3
import time
from os import environ
from jose import jwk, jwt
from jose.utils import base64url_decode

region = environ['AWS_REGION']
user_pool_id = environ['UserPoolId']

dynamodb = boto3.resource('dynamodb', region_name=environ['AWS_REGION'])
table = dynamodb.Table(environ['TableName'])

keys_url = f'https://cognito-idp.{region}.amazonaws.com/{user_pool_id}/.well-known/jwks.json'
# Downloading the public keys
response = requests.get(keys_url)
response = response.json()
keys = response['keys']


def decode_id_token(token):
    # Get the kid from the headers prior to verification
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']

    # Search for the kid in the downloaded public keys
    key_index = -1
    for idx in range(len(keys)):
        if kid == keys[idx]['kid']:
            key_index = idx
            break
    if key_index == -1:
        print('Public key not found in jwks.json')
        return {}

    # Construct the public key
    public_key = jwk.construct(keys[key_index])

    # Get the last two sections of the token,
    # message and signature (encoded in base64)
    message, encoded_signature = str(token).rsplit('.', 1)

    # Decode the signature
    decoded_signature = base64url_decode(encoded_signature.encode('utf-8'))

    # Verify the signature
    if not public_key.verify(message.encode("utf8"), decoded_signature):
        print('Signature verification failed')
        return {}

    # Use the unverified claims
    claims = jwt.get_unverified_claims(token)

    # Verifing the token expiration
    if time.time() > claims['exp']:
        print('Token is expired')
        return {}

    return claims


def generate_policy(principal_id, effect='Deny', resource=''):
    auth_response = dict()
    auth_response['principalId'] = principal_id

    policy_document = dict()
    policy_document['Version'] = '2012-10-17'
    policy_document['Statement'] = [
        {
            'Action': 'execute-api:Invoke',
            'Effect': effect,
            'Resource': resource
        }
    ]

    auth_response['policyDocument'] = policy_document
    return auth_response


def lambda_handler(event, context):
    principal_id = 'api-gateway'
    
    try:
        claims = decode_id_token(event['authorizationToken'])
        principal_id = claims['email']

        response = table.get_item(
            Key={
                'Email': principal_id
            },
            ProjectionExpression='Groups'
        )
        
        if 'Admin' not in response['Item']['Groups']:
            raise Exception()
    except Exception:
        return generate_policy(principal_id, 'Deny', event['methodArn'])

    return generate_policy(principal_id, 'Allow', event['methodArn'])
