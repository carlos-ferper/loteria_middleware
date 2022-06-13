from email_validator import validate_email, EmailNotValidError
import random as rd


def validar_email(email: str):
    try:
        email = validate_email(email).email
        return True
    except EmailNotValidError as e:
        return False


def validar_cpf(cpf: str):
    cpf = [int(char) for char in cpf if char.isdigit()]

    if len(cpf) != 11:
        return False
    if cpf == cpf[::-1]:
        return False

    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def validar_saldo():
    valor = rd.randint(1, 10)
    return valor > 3
