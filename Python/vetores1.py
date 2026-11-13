notas = []
totalNotas = 0
acimaMedia = 0
for i in range (1, 11):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    totalNotas
    if nota >= 7:
        acimaMedia += 1

media = totalNotas / 10
maior = max(notas)
maiorPosicao = notas.index(maior)
print(f"Média: {media}")
print(f"Alunos acima da média: {acimaMedia}")
print(f"Maior nota: {maior}")
print(f"Posição da maior nota: {maiorPosicao}")