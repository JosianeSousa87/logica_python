from cores import *

tarefas = []
LARGURA = 30


def cabecalho(texto, cor):
    print()
    print(cor + ESTILO_NEGRITO + "╔" + "═" * LARGURA + "╗" + RESET)
    print(cor + ESTILO_NEGRITO + "║" + texto.center(LARGURA) + "║" + RESET)
    print(cor + ESTILO_NEGRITO + "╚" + "═" * LARGURA + "╝" + RESET)


def linha():
    print(FRENTE_CINZA + "─" * (LARGURA + 2) + RESET)


def sucesso(texto):
    print(FRENTE_VERDE_CLARO + "✔ " + texto + RESET)


def erro(texto):
    print(FRENTE_VERMELHO_CLARO + "✖ " + texto + RESET)


def menu():
    cabecalho("MENU", FRENTE_AMARELO)
    print(f"{FRENTE_AMARELO}1{RESET} {FRENTE_CINZA}│{RESET} Adicionar Tarefa")
    print(f"{FRENTE_AMARELO}2{RESET} {FRENTE_CINZA}│{RESET} Listar Tarefas")
    print(f"{FRENTE_AMARELO}3{RESET} {FRENTE_CINZA}│{RESET} Remover Tarefa")
    print(f"{FRENTE_AMARELO}4{RESET} {FRENTE_CINZA}│{RESET} Sair")
    linha()


def adicionarTarefa():
    tarefa = input(FRENTE_CIANO + "➜ Digite o nome da tarefa: " + RESET)
    tarefas.append(tarefa)
    sucesso("Tarefa adicionada!")


def listarTarefas():
    cabecalho("TAREFAS", FRENTE_CIANO)

    if len(tarefas) == 0:
        print(FRENTE_CINZA + "Nenhuma tarefa cadastrada" + RESET)
    else:
        for numero, tarefa in enumerate(tarefas, start=1):
            print(f"{FRENTE_AMARELO}{numero:>2}{RESET} {FRENTE_CINZA}│{RESET} {tarefa}")

        linha()
        print(FRENTE_VERDE + f"Total: {len(tarefas)} tarefa(s)" + RESET)


def removerTarefa():
    listarTarefas()

    if len(tarefas) > 0:
        numero = int(input(FRENTE_CIANO + "\n➜ Digite o número da tarefa a remover: " + RESET))

        if 1 <= numero <= len(tarefas):
            removida = tarefas.pop(numero - 1)
            sucesso(f"Tarefa '{removida}' removida!")
        else:
            erro("Número inválido")


opcao = ""

while opcao != "4":
    menu()
    opcao = input(FRENTE_CIANO + "➜ Escolha uma opção: " + RESET)

    if opcao == "1":
        adicionarTarefa()
    elif opcao == "2":
        listarTarefas()
    elif opcao == "3":
        removerTarefa()
    elif opcao == "4":
        print(FRENTE_MAGENTA_CLARO + "\nAté mais!" + RESET)
    else:
        erro("Opção inválida")