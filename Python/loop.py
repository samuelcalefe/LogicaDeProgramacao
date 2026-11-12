somaNota = 0.0
amountNota = int(input("Quantas notas serão digitadas: "))
for contador in range (amountNota):
    nota = float(input("Digite a sua nota: "))
    somaNota += nota
media = somaNota / amountNota
print("A media das notas é", media)