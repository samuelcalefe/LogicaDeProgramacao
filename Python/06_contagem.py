# Definir um número e o intervalo
inicio = int(input("Defina um número de início: "))
intervalo = int(input("Defina o intervalo: "))

# Repetição
for i in range (inicio, -1, -intervalo):
    print(i)

# Mensagem de fim
print("Fim")
