# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
# Funções para cada operação
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

# Menu da calculadora
def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

# Programa principal
while True:
    # Exibe o menu
    menu()
    
    # Recebe a escolha do usuário
    escolha = input("Digite sua escolha (1/2/3/4) ou 's' para sair: ")
    
    # Opção de sair do loop
    if escolha == 's':
        print("Saindo da calculadora...")
        break

    # Verifica se a escolha é válida
    if escolha in ['1', '2', '3', '4']:
        # Pede os números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Realiza a operação de acordo com a escolha
        if escolha == '1':
            print(f"{num1} + {num2} = {adicao(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif escolha == '4':
            resultado = divisao(num1, num2)
            print(f"{num1} / {num2} = {resultado}")
    else:
        print("Escolha inválida. Tente novamente.")


