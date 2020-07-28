from flask import Flask, jsonify, request
from json import dumps
#from flask_cors import CORS
from secrets import randbelow
from sys import argv
from os import environ

entity_id = ''

app = Flask(__name__)
# CORS(app)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'home': '/'})


@app.route('/rota', methods=['GET'])
def rota():
    headers = list()
    for header, value in request.headers:
        headers.append(header + '=' + value)
    print(dumps({
        'endpoint': '/rota',
        'headers': headers
    }))
    routes = [
        {
            'id': entity_id,
            'carga': 'carga 1',
            'placa': 'TXT-0001',
            'frota': 'frota 1',
            'matriculaMotorista': '000-0001',
            'nomeMotorista': 'Jõao da Silva',
            'dataCarga': '2020-03-18',
            'dataSaida': '2020-03-19',
            'unidCarga': 1
        },
        {
            'id': entity_id + 1,
            'carga': 'carga 2',
            'placa': 'TXT-0001',
            'frota': 'frota 1',
            'matriculaMotorista': '000-0001',
            'nomeMotorista': 'Jõao da Silva',
            'dataCarga': '2020-03-18',
            'dataSaida': '2020-03-19',
            'unidCarga': 2
        }
    ]
    return jsonify(routes)


@app.route('/rota/find', methods=['GET'])
def find():
    headers = list()
    for header, value in request.headers:
        headers.append(header + '=' + value)
    print(dumps({
        'endpoint': '/rota/find',
        'headers': headers
    }))
    route_id = request.args.get('carga', 'N/A')
    carga = {
        'id': entity_id,
        'carga': 'carga ' + route_id,
        'placa': 'TXT-0001',
        'frota': 'frota 1',
        'matriculaMotorista': '000-0001',
        'nomeMotorista': 'Jõao da Silva',
        'dataCarga': '2020-03-18',
        'dataSaida': '2020-03-19',
        'unidCarga': 1
    }
    return jsonify(carga)


@app.route('/position/last', methods=['GET'])
def last():
    headers = list()
    for header, value in request.headers:
        headers.append(header + '=' + value)
    print(dumps({
        'endpoint': '/position/last',
        'headers': headers
    }))
    placa = request.args.get('placa', 'N/A')
    location = {
        'id': entity_id,
        'latitude': '-16.702327',
        'longitude': '-49.270078',
        'idPosicao': 1,
        'datahora': '2020-03-19T11:26:11',
        'placa': placa
    }
    return jsonify(location)


@app.route('/position/allDay', methods=['GET'])
def allDay():
    headers = list()
    for header, value in request.headers:
        headers.append(header + '=' + value)
    print(dumps({
        'endpoint': '/position/allDay',
        'headers': headers
    }))
    placa = request.args.get('placa', 'N/A')
    dia = request.args.get('dia', 'N/A')
    locations = [
        {
            'id': entity_id,
            'latitude': '-16.702327',
            'longitude': '-49.270078',
            'idPosicao': 1,
            'datahora': '2020-03-19T11:26:11',
            'placa': placa,
            'dia': dia
        },
        {
            'id': entity_id + 1,
            'latitude': '-16.705119',
            'longitude': '-49.267887',
            'idPosicao': 1,
            'datahora': '2020-03-19T11:26:11',
            'placa': placa,
            'dia': dia
        }
    ]
    return jsonify(locations)


@app.route('/roteiro', methods=['GET'])
def roteiro():
    carga = request.args.get('carga', 'N/A')
    client = {
        'id': entity_id,
        'idCliente': 1,
        'numeroPedido': 20,
        'rota': '001',
        'idEquipamento': 'e-001',
        'idMotorista': '000-0001',
        'dataPartidaRota': '2020-03-18',
        'dataChegadaRota': '2020-03-19',
        'dataPartidaParada': '2020-03-18',
        'dataChegadaParada': '2020-03-19',
        'numeroParada': 5,
        'tipoParada': 'normal',
        'fantasiaCliente': 'Padoca',
        'latitude': '-16.702327',
        'longitude': '-49.270078',
        'razaoCliente': 'Padoca Ltda.',
        'carga': carga
    }
    return jsonify(client)


@app.route('/page/<int:page_id>', methods=['GET'])
def page(page_id):
    msg = 'searched for page ' + str(page_id)
    return jsonify({
        'entity_id': entity_id,
        'msg': msg
    })


@app.route('/page/<int:page_id>/subpath', methods=['GET'])
def subpath(page_id):
    msg = 'searched for page ' + str(page_id) + ' on subpath'
    return jsonify({
        'entity_id': entity_id,
        'msg': msg
    })


@app.route('/environment', methods=['GET'])
def environment():
    api_key = environ.get('API_KEY', 'empty')
    return jsonify({
        'entity_id': entity_id,
        'api_key': api_key
    })


if __name__ == '__main__':
    entity_id = randbelow(100)

    if len(argv) != 3:
        server_ip = '0.0.0.0'
        server_port = '80'
    else:
        server_ip = argv[1]
        server_port = argv[2]
    app.run(host=server_ip, port=server_port)
