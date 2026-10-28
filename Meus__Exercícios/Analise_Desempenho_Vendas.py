# Lista de dicionários com os dados das lojas
vendas_lojas = [
    {"loja": "São Paulo (Centro)", "vendas": 1450, "vendedores": 12},
    {"loja": "Rio de Janeiro (Copacabana)", "vendas": 980, "vendedores": 8},
    {"loja": "Belo Horizonte (Savassi)", "vendas": 1200, "vendedores": 10},
    {"loja": "Curitiba (Centro Cívico)", "vendas": 750, "vendedores": 6},
    {"loja": "Salvador (Barra)", "vendas": 1320, "vendedores": 11}
]

meta_minima = 1000

# Escreva a sua lógica abaixo desta linha:

#Erros durante o processo:
#vendas = (1450, 980, 1200, 750, 1320) - Eu apaguei tanto este, quanto o de baixo, pois estão redundantes, já estão definidos no dicionário vendas_lojas.
#vendedores = (12, 8, 10, 6, 11)

#1º Erro:
#soma = sum(vendas)
#print(f"Total de vendas das lojas: {soma}")
#soma = sum(vendas)

#2º Erro
#maior_resultado = max(vendas_lojas)
#print(f"A loja com maior resultado de vendas é: {vendas_lojas}")

#3º Erro:
#maior_resultado = max(vendas_lojas, key=lambda x: x[vendas_lojas])

#4º Erro:
#if [vendas_lojas] >= meta_minima :
#    print(f"As lojas que bateram a meta foram: ["loja"] com o total de vendas ["vendas"]")

#4º Erro:
#print("\n")
#for loja in vendas_lojas:
#     media = loja["vendas"] % loja["vendedores"]
#     print(f"A média de vendas por vendedores é de: {loja['loja']}: {media:.2f}, sendo o total de vendedores {loja["vendedores"]}.")

soma = sum(loja["vendas"] for loja in vendas_lojas)
print(f"Total de vendas das lojas: {soma}.\n")

maior_resultado = max(vendas_lojas, key=lambda x: x["vendas"])
print(f"A loja com o maior resultado de vendas é {maior_resultado["loja"]} com {maior_resultado["vendas"]} vendas.\n")

maior_vendedores = max(vendas_lojas, key=lambda x: x["vendedores"])
print(f"A loja com o maior número de vendedores é {maior_vendedores["loja"]} com {maior_vendedores["vendedores"]}.\n")

for loja in vendas_lojas:
    if loja["vendas"] >= meta_minima:
        print(f"As lojas que bateram a meta foram: {loja['loja']} com {loja['vendas']} vendas.")
#    else:
#        print(f"As lojas que não bateram a meta foram: {loja['loja']} com {loja['vendas']} vendas.")

print("\n")
for loja in vendas_lojas:
    if loja["vendas"] < meta_minima:
        print(f"As lojas que não bateram a meta foram: {loja['loja']} com {loja['vendas']} vendas.")

print("\n")
for loja in vendas_lojas:
    if loja["vendas"] >= meta_minima:
                print(f"Meta Batida 🚀: {loja['loja']}.")

print("\n")
for loja in vendas_lojas:
    if loja["vendas"] < meta_minima:
        print(f"Precisa de Atenção ⚠️: {loja['loja']}.")

print("\n")
for loja in vendas_lojas:
     media = loja["vendas"] / loja["vendedores"]
     print(f"A média de vendas por vendedores é de: {loja['loja']}: {media:.2f}, sendo o total de {loja["vendedores"]} vendedores.")

#for loja in vendas_lojas:
#    if loja["vendas"] >= meta_minima:
#        print(f"Meta Batida 🚀 {loja['loja']}.")
#    else:
#        print(f"Precisa de Atenção ⚠️ {loja['loja']}.")