nomes = []
vendas = []
comissoes = []
receber = []

for i in range(10):
    nome = input("Nome: ")
    venda = float(input("Total de vendas: "))
    comissao = float(input("Percentual de comissão: "))
    
    nomes.append(nome)
    vendas.append(venda)
    comissoes.append(comissao)
    receber.append(venda * (comissao / 100))

total = sum(vendas)
maior = max(receber)
menor = min(receber)

nome_maior = nomes[receber.index(maior)]
nome_menor = nomes[receber.index(menor)]

print("\na) Relatório de valores a receber:")
for i in range(10):
    print(f"{nomes[i]}: R$ {receber[i]:.2f}")

print(f"\nb) Total das vendas: R$ {total:.2f}")
print(f"c) Maior valor: R$ {maior:.2f} - Vendedor: {nome_maior}")
print(f"d) Menor valor: R$ {menor:.2f} - Vendedor: {nome_menor}")