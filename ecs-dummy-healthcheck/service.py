from flask import Flask, jsonify, request
from os import environ

app = Flask(__name__)

service_host = environ.get('SRV_HOST', '0.0.0.0')
service_port = environ.get('SRV_PORT', '80')


# Answer to GET requests at any path
@app.route('/',  methods=['GET'])
def home():
    return jsonify({'200': 'OK'})


@app.route('/<path:url>',  methods=['GET'])
def check_get(url):
    return jsonify({'url': url})


# Answer to POST requests at any path
@app.route('/',  methods=['POST'])
def home_post():
    data = request.get_json()
    try:
        return jsonify(data)
    except:
        pass
    return jsonify({'200': 'OK'})


@app.route('/<path:url>', methods=['POST'])
def check_post(url):
    data = request.get_json()
    try:
        return jsonify(data)
    except:
        pass
    return jsonify({'200': 'OK'})

if __name__ == '__main__':
    app.run(host=service_host, port=service_port)
