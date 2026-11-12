# Variáveis
salario = 0
somaSalario = 0
maiorSalario = 0
qtdMenor100 = 0
qtdPessoas = 0
filhos = 0
somaFilhos = 0

# Recebe informações
while salario >= 0:
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        break
    filhos = int(input("Digite a quantidade de filhos: "))
    qtdPessoas += 1
    somaSalario += salario
    somaFilhos += filhos

    if maiorSalario < salario:
        maiorSalario = salario
    if salario < 100:
        qtdMenor100 += 1


    print("A média dos salários é", (somaSalario / qtdPessoas))
    print("A média dos filhos é", (somaFilhos / qtdPessoas))
    print("Maior salário:", maiorSalario)
    print("Percentual das pessoas com até 100: ", (qtdMenor100 * 100 / qtdPessoas))
