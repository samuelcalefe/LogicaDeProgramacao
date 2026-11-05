# Inicia o contador de negativos
contador = 0

#Leitura inicial
numero = int(input("Digite um número negativo (ou 0 para sair): "))
while numero != 0:
    # Verifica os números
    if numero < 0:
        contador += 1

# Atualização e repetição
    numero = int(input("Digite outro número negativo (ou 0 para sair): "))

# Exibição
print(f"\nVocê digitou {contador} números negativos.")