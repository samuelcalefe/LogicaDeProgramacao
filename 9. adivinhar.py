import random
numero = random.randint(1,50)
errou = 1

print("Adivinhe um número entre 1 e 50")
for contador in range (5):
    num = int(input("Digite um valor: "))
    if num == numero:
        print("Acertou!")
        errou = 0
        break
    elif num > numero:
        print("Muito grande, tente novamente.")
    elif num < numero:
        print("Muito pequeno. Tente novamente.")
    else:
        print("Tente novamente.")
    
if(errou == 1):
    print("O número era", numero)
