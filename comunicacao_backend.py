import requests
import json
from rotas_backend import *


class Sender:

    @staticmethod
    def logar_backend(dicionario: dict):
        url = LOGIN
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)

    @staticmethod
    def aumentar_saldo(dicionario: dict):
        url = AUMENTAR_SALDO
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)

    @staticmethod
    def criar_sorteio(dicionario: dict):
        url = CRIAR_SORTEIO
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)

    @staticmethod
    def listar_sorteios(dicionario: dict):
        url = LISTAR_SORTEIOS
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)

    @staticmethod
    def comprar_ingresso(dicionario: dict):
        url = COMPRAR_INGRESSO
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)

    @staticmethod
    def sortear(dicionario: dict):
        url = COMPRAR_INGRESSO
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)

    @staticmethod
    def listar_ingressos(dicionario: dict):
        url = LISTAR_INGRESSOS
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)

    @staticmethod
    def criar_usuario(dicionario: dict):
        url = CRIAR_USUARIO
        response = requests.post(url, data=json.dumps(dicionario))

        return json.loads(response.text)
