from flask import Flask, request, jsonify
from control import Control

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def logar():
    input_json = request.get_json(force=True)
    return Control.login(input_json)


@app.route('/aumentar_saldo', methods=['POST'])
def aumentar_saldo():
    input_json = request.get_json(force=True)

    return Control.aumentar_saldo(input_json)


@app.route('/criar_sorteio', methods=['POST'])
def criar_sorteio():
    input_json = request.get_json(force=True)

    return Control.criar_sorteio(input_json)


@app.route('/comprar_ingresso', methods=['POST'])
def comprar_ingresso():
    input_json = request.get_json(force=True)

    return Control.comprar_ingresso(input_json)


@app.route('/sortear', methods=['POST'])
def sortear():
    input_json = request.get_json(force=True)

    return Control.sortear(input_json)


@app.route('/listar_sorteios', methods=['POST'])
def listar_sorteios():
    input_json = request.get_json(force=True)

    return Control.listar_sorteios(input_json)


@app.route('/listar_ingressos_do_usuario', methods=['POST'])
def listar_ingressos():
    input_json = request.get_json(force=True)

    return Control.listar_ingressos(input_json)

