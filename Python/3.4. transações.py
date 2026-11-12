comprasVista = 0
comprasPrazo = 0
totalVista = 0
totalPrazo = 0

for i in range(1, 16):
    print("--------------------------------")
    valor = float(input(f"Digite o valor da {i}º compra: "))
    while valor < 0:
        valor = float(input("Digite um valor válido: "))
    print("[1] - Vista | [2] - Prazo")
    codigo = int(input("Digite o código: "))
    while codigo not in [1, 2]:
        codigo = int(input("Digite um código válido: "))

    if codigo == 1:
        print("Compra à vista.")
        comprasVista += 1
        totalVista += valor

    elif codigo == 2:
        print("Compra à prazo.")
        comprasPrazo += 1
        totalPrazo += valor

print("--------------------------------")
print(f"Total de compras à vista: {comprasVista}")
print(f"Total de compras à prazo: {comprasPrazo}")
print(f"Soma das compras à vista: {totalVista}")
print(f"Soma das compras à prazo: {totalPrazo}")
print(f"Valor da primeira prestação das compras à prazo: {comprasPrazo / 3}")