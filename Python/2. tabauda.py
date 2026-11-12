# Entrada de dados
numero = int(input("Digite a tabuada: "))
limite = int(input("Digite até qual número deseja multiplicar: "))

# Repetição
for i in range(1, limite + 1):
    # Cálculo e exibição
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
