# Inicia variável e pede quantos números vai ser a média
somaNota = 0.0
qtdPar = 0.0
qtdNota = int(input("Digite quantas notas vai medir: "))

# Repetição
for i in range(qtdNota):
    #Verifica se a nota é par, e se for, inclui ela
    nota = int(input("Digite a sua nota: "))
    if nota % 2 == 0:
        qtdPar += 1
        somaNota += nota

# Verifica se há notas pares para calcular o resultado
if qtdPar > 0:
    media = somaNota / qtdPar
    print(f"A media das notas é {media}")
else:
    print("Nenhuma nota par.")