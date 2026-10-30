from cores import *
LARGURA = 28

def cabecalho(texto, cor):
    print()    
    print(cor + ESTILO_NEGRITO + ("✿.*･" * 7) + RESET)    
    print(cor + ESTILO_NEGRITO + "★ " + texto.center(LARGURA - 4) + " ★" + RESET)
    print(cor + ESTILO_NEGRITO + ("✿.*･" * 7) + RESET)

def linha():
    print(FRENTE_BRANCO_CLARO + "─" * LARGURA + RESET)

def sucesso(texto):
    print(FRENTE_VERDE_CLARO + "✔ " + texto + RESET)

def erro(texto):
    print(FRENTE_VERMELHO_CLARO + "✖ " + texto + RESET)

def menu():
    cabecalho("CALCULADORA", FRENTE_MAGENTA_CLARO)    
    print(f"  {FRENTE_AMARELO}1{RESET} {FRENTE_BRANCO_CLARO}│{RESET} Iniciar Calculadora")
    print(f"  {FRENTE_AMARELO}2{RESET} {FRENTE_BRANCO_CLARO}│{RESET} Sair")
    linha()

def ehinteiro(numero):    
    if numero % 1 == 0:
        return True
    else:
        return False    

def ehpar(numero):
    if not ehinteiro(numero):
        return False
    if numero % 2 == 0:
        return True
    else:
        return False

def exibir_teclado(resultado_atual):    
    visor = str(resultado_atual).center(26)
    
    print()
    print(FRENTE_VERDE_CLARO + ESTILO_NEGRITO + " ┌──────────────────────────┐" + RESET)
    print(FRENTE_VERDE_CLARO + ESTILO_NEGRITO + f" │{visor}│" + RESET)
    print(FRENTE_VERDE_CLARO + ESTILO_NEGRITO + " └──────────────────────────┘" + RESET)
    print()
    
    print(FRENTE_CINZA + "  [ C ]  [ ⌫ ]  [ % ]  " + FRENTE_BRANCO_CLARO + "[ ÷ ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ 7 ]  [ 8 ]  [ 9 ]  [ × ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ 4 ]  [ 5 ]  [ 6 ]  [ - ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ 1 ]  [ 2 ]  [ 3 ]  [ + ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ ± ]  [ 0 ]  [ , ]  " + FRENTE_MAGENTA_CLARO + "[ = ]" + RESET)
    print()

    if ehpar(resultado_atual) == True:
        texto_par = "Par"
    else:
        texto_par = "Ímpar"

    if ehinteiro(resultado_atual) == True:
        texto_inteiro = "Inteiro"
    else:
        texto_inteiro = "Decimal"

    print(f"  {FRENTE_BRANCO_CLARO}{resultado_atual}   {FRENTE_BRANCO_CLARO}➜ {FRENTE_AMARELO_CLARO}{texto_par}{RESET}")
    print(f"  {FRENTE_BRANCO_CLARO}{resultado_atual}   {FRENTE_BRANCO_CLARO}➜ {FRENTE_AMARELO_CLARO}{texto_inteiro}{RESET}")
    linha()    

def modo_infinito():
    cabecalho("CALCULADORA", FRENTE_MAGENTA_CLARO)    
    acumulado = 0
    exibir_teclado(acumulado)
        
    acumulado = float(input(FRENTE_CIANO_CLARO + "➜ Digite o número inicial: " + RESET))
        
    while True:    
        cabecalho("CONTA EM ANDAMENTO", FRENTE_MAGENTA_CLARO)
        exibir_teclado(acumulado)
        
        operador = input(FRENTE_CIANO_CLARO + "➜ Escolha o operador (+, -, *, /, =): " + RESET)
        
        
        if operador == "=":
            cabecalho("RESULTADO FINAL", FRENTE_VERDE)
            exibir_teclado(acumulado)
            sucesso(f"Cálculo finalizado! Total: {acumulado}")
            break
                
        if operador in ["+", "-", "*", "/"]:
            proximo_num = float(input(FRENTE_CIANO_CLARO + "➜ Digite o próximo número: " + RESET))
                
            if operador == "+":
                acumulado += proximo_num
            elif operador == "-":
                acumulado -= proximo_num
            elif operador == "*":
                acumulado *= proximo_num
            elif operador == "/":
                if proximo_num == 0:
                    erro("Não é possível dividir por zero! Operação ignorada.")
                else:
                    acumulado /= proximo_num
        else:
            erro("Operador inválido! Use apenas +, -, *, / ou =")

opcao = ""

while opcao != "2":
    menu()
    opcao = input(FRENTE_CIANO_CLARO + "➜ Escolha uma opção: " + RESET)

    if opcao == "1":
        modo_infinito()
    elif opcao == "2":
        print(FRENTE_MAGENTA_CLARO + "\nAté mais!" + RESET)
    else:
        erro("Opção inválida")