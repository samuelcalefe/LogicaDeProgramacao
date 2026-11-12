n = int(input("Digite um número inteiro: "))
for linha in range(1, n + 1):
 
    for coluna in range(1, linha + 1):
        print(coluna, end=" ")
        
    print()