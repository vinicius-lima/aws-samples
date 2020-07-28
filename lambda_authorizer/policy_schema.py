import json


def generate_policy(principal_id, effect='Deny', resource=''):
    # It is necessary to use a wildcard endpoint due to Api Gateway cache
    resource = resource.split('/')
    resource[-1] = '*'
    resource = '/'.join(resource)

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
    print(json.dumps(event))
    principal_id = 'api-gateway'
    return generate_policy(principal_id, 'Allow', event['methodArn'])
