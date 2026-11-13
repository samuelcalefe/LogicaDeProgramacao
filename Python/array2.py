numeros = []
pares = []
impares = []
for i in range (1, 7):
    i = int(input("Digite um número: "))
    numeros.append(i)
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(numeros)
print(f"Pares:{pares}")
print(f"Ímpares:{impares}")