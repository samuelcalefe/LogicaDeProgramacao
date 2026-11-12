nao_perecivel = 0
perecivel = 0
vestuario = 0
higiene = 0
limpeza = 0

while True:
    print("---------------------------------------------------------------------------------------------")
    print("nao_perecivel = 1 | perecivel = 2 a 4 | vestuario = 5 e 6 | higiene = 7 | limpeza = 8 a 15")
    print("---------------------------------------------------------------------------------------------")
    try:
        codigo = int(input("Digite o código do produto (ou 0 para finalizar): "))
    except ValueError:
        print("Digite apenas números inteiros.")
        continue

    if codigo == 1:
        print("Item registrado como Não Perecível.")
        nao_perecivel += 1

    elif codigo >= 2 and codigo <= 4:
        print("Item registrado como Perecível.")
        perecivel += 1

    elif codigo == 5 or codigo == 6:
        print("Item registrado como Vestuário.")
        vestuario += 1

    elif codigo == 7:
        print("Item registrado como Higiene Pessoal.")
        higiene += 1

    elif codigo >= 8 and codigo <= 15:
        print("Item registrado como Limpeza e Utensílios Domésticos.")
        limpeza += 1

    elif codigo == 0:
        print("Programa finalizado. Resultados:")
        print(f"nao_perecivel = {nao_perecivel} \nperecivel = {perecivel} \nvestuario = {vestuario} \nhigiene = {higiene} \nlimpeza = {limpeza}")
        print("---------------------------------------------------------------------------------------------")
        break

    else:
        print("Inválido.")