from cores import *
LARGURA = 28 # Mudamos para 28 para casar perfeitamente com a largura dos botões

def cabecalho(texto, cor):
    print()    
    # "✿.*･" repetido 7 vezes dá 28 caracteres certinhos para o teto e chão
    print(cor + ESTILO_NEGRITO + ("✿.*･" * 7) + RESET)      
    # Ajustamos para LARGURA - 4 para compensar o espaço das estrelas e cravar nos 28
    print(cor + ESTILO_NEGRITO + "★ " + texto.center(LARGURA - 4) + " ★" + RESET)        
    print(cor + ESTILO_NEGRITO + ("✿.*･" * 7) + RESET)

def linha():
    # Desenha a linha branca com exatamente 28 traços para alinhar com os botões
    print(FRENTE_BRANCO_CLARO + "─" * LARGURA + RESET)

def sucesso(texto):
    print(FRENTE_VERDE_CLARO + "✔ " + texto + RESET)

def erro(texto):
    print(FRENTE_VERMELHO_CLARO + "✖ " + texto + RESET)

def menu():
    cabecalho("CALCULADORA", FRENTE_MAGENTA_CLARO)
    # Adicionamos espaços manuais para as opções do menu ficarem centralizadas na largura 28
    print(f"  {FRENTE_AMARELO}1{RESET} {FRENTE_BRANCO_CLARO}│{RESET} Iniciar Calculadora")
    print(f"  {FRENTE_AMARELO}2{RESET} {FRENTE_BRANCO_CLARO}│{RESET} Sair")
    linha()

def exibir_teclado(resultado_atual):
    # Para o visor não estourar com o caractere gordinho '║', usamos o '│' que tem tamanho 1 perfeito no seu terminal
    # Centralizamos o texto em 26 espaços. 26 espaços + 2 paredes '│' = 28 de largura total!
    visor = str(resultado_atual).center(26)
    
    print()
    print(FRENTE_VERDE_CLARO + ESTILO_NEGRITO + " ┌──────────────────────────┐" + RESET)
    print(FRENTE_VERDE_CLARO + ESTILO_NEGRITO + f" │{visor}│" + RESET)
    print(FRENTE_VERDE_CLARO + ESTILO_NEGRITO + " └──────────────────────────┘" + RESET)
    print()
    
    # Fileiras de botões (todas têm exatamente 28 caracteres de largura)
    print(FRENTE_CINZA + "  [ C ]  [ ⌫ ]  [ % ]  " + FRENTE_BRANCO_CLARO + "[ ÷ ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ 7 ]  [ 8 ]  [ 9 ]  [ × ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ 4 ]  [ 5 ]  [ 6 ]  [ - ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ 1 ]  [ 2 ]  [ 3 ]  [ + ]" + RESET)
    print(FRENTE_BRANCO_CLARO + "  [ ± ]  [ 0 ]  [ , ]  " + FRENTE_MAGENTA_CLARO + "[ = ]" + RESET)
    linha()




def modo_infinito():
    cabecalho("CALCULADORA", FRENTE_MAGENTA_CLARO)
    
    # 1. Iniciamos o acumulador com 0 e exibimos o teclado inicial
    acumulado = 0
    exibir_teclado(acumulado)
    
    # 2. Capturamos o primeiro número para iniciar os cálculos
    acumulado = float(input(FRENTE_CIANO_CLARO + "➜ Digite o número inicial: " + RESET))
    
    # 3. Abrimos o loop de cálculo em cadeia
    while True:
        # Atualizamos o visual do teclado mostrando o número atual no visor verde
        cabecalho("CONTA EM ANDAMENTO", FRENTE_MAGENTA_CLARO)
        exibir_teclado(acumulado)
        
        operador = input(FRENTE_CIANO_CLARO + "➜ Escolha o operador (+, -, *, /, =): " + RESET)
        
        # Condição de Parada: Se o usuário apertar '=', o loop quebra
        if operador == "=":
            cabecalho("RESULTADO FINAL", FRENTE_VERDE)
            exibir_teclado(acumulado)
            sucesso(f"Cálculo finalizado! Total: {acumulado}")
            break
            
        # Se não for '=', o programa precisa pedir o próximo número para calcular
        if operador in ["+", "-", "*", "/"]:
            proximo_num = float(input(FRENTE_CIANO_CLARO + "➜ Digite o próximo número: " + RESET))
            
            # Executamos a matemática nos bastidores baseado no operador escolhido
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