temp = []
mediaTemp = []
temperaturas = 0
somaTemp = 0

for i in range (1, 122):
    i = float(input("Digite a temperatura: "))
    temperaturas += 1
    somaTemp += i
    temp.append(i)

maior = max(temp)
menor = min(temp)
media = somaTemp / temperaturas

print(f"Maior temperatura: {maior}")
print(f"Menor temperatura: {menor}")
print(f"Média das temperaturas: {media}")