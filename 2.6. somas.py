pares = 0
impar = 0
pos = 0
neg = 0

while True: 
    print("--------------------------------------------------------")
    num = int(input("Digite um número (ou 0 para finalizar): "))

    if num > 0:
        print("Número positivo.")
        pos += 1
    elif num < 0:
        print("Número negativo.")
        neg += 1
    elif num % 2 == 0:
        pares += 1
    elif num % 3 == 0:
        impar += 1

    if num == 0:
        print("--------------------------------------------------------")
        print("Finalizado. Resultados:")
        print(f"Números positivos: {pos} \nNúmeros negativos: {neg}")
        print(f"Soma dos positivos com negativos: {pos + neg}")
        print(f"Números pares: {pares} \nNúmeros ímpares: {impar}")
        print("--------------------------------------------------------")
        break
