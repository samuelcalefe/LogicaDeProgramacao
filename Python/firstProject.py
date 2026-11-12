numero = 5 #inteiro
numero2 = 5.5 #float
nome = "gues" #string
opcao = True #Boolean
print(numero)

num = int(input("Digite um valor: "))

if num > 5 and num < 10:
    print("Maior que 5 e menor que 10")
elif num == 5 or num != 5:
    print("Igual a 5")
else:
    print("Menor que 5")