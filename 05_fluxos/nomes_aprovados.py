nomes_aprovados = ["João", "Maria", "Pedro", "Mariana", "Josiane"]
for n in nomes_aprovados:
    print(n)

# strip() remove os espaços quando digitarem
nome = input("Digite o seu nome: ").strip() 

#para converter as letras digitadas em minúsculas:
if nome.lower() in [n.lower() for n in nomes_aprovados]:
    print(f"{nome} aprovado!")
else:
    print(f"{nome} reprovado!")

#string é uma lista de caracter