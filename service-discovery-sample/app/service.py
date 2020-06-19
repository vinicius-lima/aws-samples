from flask import Flask, jsonify, request
from secrets import token_hex
from os import environ
import requests

app = Flask(__name__)

service_id = token_hex(2)
service_name = environ['SRV_NAME']
service_host = environ['SRV_HOST']
service_port = environ['SRV_PORT']
remote_host = environ['REMOTE_HOST']
remote_port = environ['REMOTE_PORT']


@app.route('/',  methods=['GET'])
def home():
    return jsonify({'name': service_name, 'id': service_id})


@app.route('/hello',  methods=['GET'])
def hello():
    client = request.args.get('client')
    client = "" if client is None else client
    return jsonify({'greetings': 'Hello ' + client + "!"})


@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    result = dict()
    try:
        result = {
            'result': int(data['a']) + int(data['b']),
            'a': data['a'],
            'b': data['b']
        }
    except:
        result = {
            'msg': 'could not sum numbers',
            'body': data
        }

    return jsonify(result)


@app.route('/remote', methods=['GET'])
def remote():
    response = requests.get('http://' + remote_host + ':' + remote_port + '/')
    response = response.json()
    return jsonify({
        'this': {
            'id': service_id,
            'name': service_name
        },
        'remote': {
            'id': response['id'],
            'name': response['name'],
            'host': remote_host,
            'port': remote_port
        }
    })


if __name__ == '__main__':
    app.run(host=service_host, port=service_port)
