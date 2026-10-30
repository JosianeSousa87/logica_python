from cores import *
LARGURA = 34

def cabecalho(texto, cor):
    print()       
    print(cor + ESTILO_NEGRITO + ("✿.*･" * 9) + "✿" + RESET)    
    print(cor + ESTILO_NEGRITO + "★ " + texto.center(LARGURA - 1) + " ★" + RESET)
    print(cor + ESTILO_NEGRITO + ("✿.*･" * 9) + "✿" + RESET)

def linha():
    print(FRENTE_BRANCO_CLARO + "-" * (LARGURA + 2) + RESET)

def sucesso(texto):
    print(FRENTE_VERDE_CLARO + "✔ " + texto + RESET)

def erro(texto):
    print(FRENTE_VERMELHO_CLARO + "✖ " + texto + RESET)

def menu():
    cabecalho("CALCULADORA", FRENTE_MAGENTA_CLARO)
    print(f"{FRENTE_AMARELO}1{RESET} {FRENTE_BRANCO_CLARO}|{RESET} Somar")
    print(f"{FRENTE_AMARELO}2{RESET} {FRENTE_BRANCO_CLARO}|{RESET} Subtrair")
    print(f"{FRENTE_AMARELO}3{RESET} {FRENTE_BRANCO_CLARO}|{RESET} Multiplicar")
    print(f"{FRENTE_AMARELO}4{RESET} {FRENTE_BRANCO_CLARO}|{RESET} Dividir")
    print(f"{FRENTE_AMARELO}5{RESET} {FRENTE_BRANCO_CLARO}|{RESET} Sair")
    linha()

def pedir_numeros():
    n1 = float(input(FRENTE_CIANO_CLARO + "➜ Digite o 1º número: " + RESET))
    n2 = float(input(FRENTE_CIANO_CLARO + "➜ Digite o 2º número: " + RESET))
    return n1, n2

def somar():
    cabecalho("OPERAÇÃO DE SOMA", FRENTE_MAGENTA_CLARO)
    n1, n2 = pedir_numeros()
    resultado = n1 + n2

    linha()
    cabecalho(f"{n1} + {n2} = {resultado}", FRENTE_VERDE_CLARO)

def subtrair():
    cabecalho("OPERAÇÃO DE SUBTRAÇÃO", FRENTE_MAGENTA_CLARO)
    n1, n2 = pedir_numeros()
    resultado = n1 - n2

    linha()
    cabecalho(f"{n1} - {n2} = {resultado}", FRENTE_VERDE_CLARO)

def multiplicar():
    cabecalho("OPERAÇÃO DE MULTIPLICAÇÃO", FRENTE_MAGENTA_CLARO)
    n1, n2 = pedir_numeros()
    resultado = n1 * n2

    linha()
    cabecalho(f"{n1} * {n2} = {resultado}", FRENTE_VERDE_CLARO)

def dividir():
    cabecalho("OPERAÇÃO DE DIVISÃO", FRENTE_MAGENTA_CLARO)
    n1, n2 = pedir_numeros

    linha()
    if n2 == 0:
        erro("Não é possível dividir por zero!")
    else:
        resultado = n1 / n2
        cabecalho(f"{n1} / {n2} = {resultado}", FRENTE_VERDE_CLARO)

opcao = ""

while opcao != "5":
    menu()
    opcao = input(FRENTE_CIANO_CLARO + "➜ Escolha uma operação: " + RESET)

    if opcao == "1":
        somar()
    elif opcao == "2":
        subtrair()
    elif opcao == "3":
        multiplicar()
    elif opcao == "4":
        dividir()
    elif opcao == "5":
        print(FRENTE_MAGENTA_CLARO + "\nAté mais!" + RESET)
    else:
        erro("Opção Inválida")