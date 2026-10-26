nome = input("Digite o nome do Aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Parabéns {nome} foi aprovado(a) com a média {media}")
elif media >=5:
    print(f"Atenção {nome}, você está de exame com a média {media}")
else:
    print(f"Caro(a) {nome} foi reprovado(a) com a média {media}")

