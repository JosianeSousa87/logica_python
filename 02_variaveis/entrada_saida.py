nome = input("Digite o seu nome: ")

# Para transformar em número, eu usar "int".
#Exemplo: numero1 = int(input("Digite o primeiro número: "))

# Para transformar em números quebrados, eu uso "float"
#Exemplo: numero1 = float(input("Digite o primeiro número: "))
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))

print(nome)
resultado = numero1 + numero2 + numero3 + numero4

print(f"{numero1} mais {numero2} mais {numero3}\n mais {numero4} = {resultado}")