num = int(input("Insira um número inteiro positivo: "))

print("\nNúmeros pares:")

if num % 2 == 0:
    
    for i in range(num, -1, -2):
        print(i)
else:
    for i in range(num - 1, -1, -2):
        print(i)

print("Fim")