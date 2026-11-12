soma_notas = 0.0
qtd_pos = 0

print("Digite números positivos (ou negativo para encerrar)")

while True:
    numero = float(input("Digite um número: "))
    
    if numero < 0:
        break
    
    if numero > 0:
        soma_notas += numero
        qtd_pos += 1

if qtd_pos > 0:
    media = soma_notas / qtd_pos
    print(f"\nA média dos números positivos é {media:.2f}")
else:
    print("\nNenhum número positivo foi digitado.")
