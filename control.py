from tools import *
from comunicacao_backend import Sender


class Control:

    @staticmethod
    def login(dicionario: dict):
        email = dicionario['email']

        if validar_email(email):
            Sender.logar_backend(dicionario)
            return True
        return False

    @staticmethod
    def aumentar_saldo(dicionario: dict):
        if 1 == 2:
            resposta = Sender.aumentar_saldo(dicionario)
            return resposta
        return {"status": False, "mensagem": "Falha ao executar o pagamento!"}

    @staticmethod
    def criar_sorteio(dicionario: dict):
        resposta = Sender.criar_sorteio(dicionario)
        return resposta

    @staticmethod
    def comprar_ingresso(dicionario: dict):
        resposta = Sender.comprar_ingresso(dicionario)
        return resposta

    @staticmethod
    def sortear(dicionario: dict):
        resposta = Sender.sortear(dicionario)
        return resposta

    @staticmethod
    def listar_ingressos(dicionario: dict):
        resposta = Sender.listar_ingressos(dicionario)
        return resposta

    @staticmethod
    def listar_sorteios(dicionario: dict):
        resposta = Sender.listar_sorteios(dicionario)
        return resposta

    @staticmethod
    def criar_usuario(dicionario: dict):
        Sender.criar_usuario(dicionario)