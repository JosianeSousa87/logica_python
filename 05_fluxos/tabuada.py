numero = int(input("Digite um número inteiro: "))

# em range precisa colocar a quantidade + 1, pois ele não delimita o último número (ex.: se eu colocar 10, ele conta até o 9, pois não considera 10)
for contador in range(0, 11, 2): # caso eu queira que ele pule a casa das contagens, eu delimito a quantidade que eu quero (ex: se eu quero que ele pule de 2 em 2, eu coloco o número 2 depois do 11)
    print(f"{numero} x {contador} = {numero * contador}")
