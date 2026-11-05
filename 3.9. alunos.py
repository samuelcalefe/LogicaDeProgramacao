total_notas = 0
alunosacima = 0
for _ in range(35):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    total_notas += nota
    if nota > 7:
        alunosacima += 1
mediaGeral = total_notas / 35
print(f"A média geral da turma é: {mediaGeral}")
print(f"A quantidade de alunos com nota acima de 7 é: {alunosacima}")