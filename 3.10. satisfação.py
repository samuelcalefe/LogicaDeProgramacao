clientebom = 0
clientepessimo = 0
clienteexcelente = 0
somaIdadeExcelente = 0
for _ in range(40):
    avaliacao = int(input("Digite a avaliação do cliente \n1 - pessimo\n2 - regular\n3 - bom\n4 - excelente\n"))
    idade = int(input("Digite a idade do cliente: "))
    if avaliacao == 4:
        clienteexcelente += 1
        somaIdadeExcelente += idade
    elif avaliacao == 1:
        clientepessimo += 1
    elif avaliacao == 3:
        clientebom += 1

if clienteexcelente > 0:
    mediaIdadeExcelente = somaIdadeExcelente / clienteexcelente
else:
    mediaIdadeExcelente = 0

porcentagemBom = (clientebom / 40) * 100

print(f"A média de idade dos clientes que avaliaram como 'excelente' é: {mediaIdadeExcelente}")
print(f"O total de clientes que avaliaram como 'péssimo' é: {clientepessimo}")
print(f"A porcentagem de clientes que avaliaram como 'bom' em relação ao total é: {porcentagemBom}%")