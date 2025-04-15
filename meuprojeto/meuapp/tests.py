from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.test import Client
from django.core import mail
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext as _
from django.utils.translation import activate
from django.utils.translation import deactivate
from django.utils.translation import get_language
from django.utils.translation import get_language_info
from django.utils.translation import get_language_bidi 

from django.test import TestCase

# Create your tests here.

#from django.urls import reverse
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
#from django.contrib.auth import authenticate
#from django.test import Client
#from django.core import mail
#from django.conf import settings
#from django.utils import timezone
#from django.utils.translation import gettext as _
#from django.utils.translation import activate
#from django.utils.translation import deactivate
#from django.utils.translation import get_language
#from django.utils.translation import get_language_info
#from django.utils.translation import get_language_bidi 

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        raise ValueError("Raiz quadrada de número negativo não é permitida.")
    return a ** 0.5

def fatorial(a):
    if a < 0:
        raise ValueError("Fatorial de número negativo não é permitido.")
    if a == 0 or a == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, a + 1):
            resultado *= i
        return resultado

operacoes = {
    '0': ('adição', adicao, '+'),
    '1': ('subtração', subtracao, '-'),
    '2': ('multiplicação', multiplicacao, '*'),
    '3': ('divisão', divisao, '/'),
    '4': ('potência', potencia, '**'),
    '5': ('raiz', raiz, 'raiz'),
    '6': ('fatorial', fatorial, '!'),
    '7': ('sair', None, 'sair'),
}

def calculadora():
    print("Bem-vindo à Calculadora Python Modular!")
    print("Selecione a operação:")
    for chave, (nome, _, _) in operacoes.items():
        print(f"{chave} - {nome}")

    while True:
        escolha = input("\nDigite o número da operação desejada (0-7): ")

        if escolha == '7':
            print("Saindo da calculadora. Até logo!")
            break
        elif escolha not in operacoes:
            print("Opção inválida! Por favor, tente novamente.")
            continue

        nome, funcao, simbolo = operacoes[escolha]

        try:
            if simbolo == 'raiz':
                num1 = float(input("Digite o número: "))
                resultado = funcao(num1)
                print(f"O resultado da {nome} de {num1} é: {resultado}")
            elif simbolo == '!':
                num1 = int(input("Digite o número inteiro: "))
                resultado = funcao(num1)
                print(f"O resultado do {nome} de {num1} é: {resultado}")
            else:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = funcao(num1, num2)
                print(f"O resultado de {num1} {simbolo} {num2} é: {resultado}")
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    calculadora()
