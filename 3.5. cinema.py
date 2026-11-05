totalOtimo = 0
somaOtimo = 0
somaRegular = 0
somaBom = 0

for i in range(15):
    idade = int(input("Digite a sua idade: "))
    print("[1] - Regular | [2] - Bom | [3] - Ótimo")
    opiniao = int(input("Opinião sobre o filme: "))
    while opiniao not in [1, 2, 3]:
        opiniao = int(input("Digite um número válido: "))
    if opiniao == 3:
        totalOtimo += 1
        somaOtimo += idade
    elif opiniao == 1:
        somaRegular += 1
    elif opiniao == 2:
        somaBom += 1

print(f"Média das idades de quem respondeu Ótimo: {somaOtimo / totalOtimo}")
print(f"Soma de quem respondeu Regular: {somaRegular}")
print("Porcentagem de quem respondeu Bom:" (somaBom / 15) * 100)