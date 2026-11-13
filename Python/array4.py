nomes = []
posicoes = int(input("Digite o número de posições:"))

while True:
    print("======== MENU ======== ")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nome")
    print("0) Sair do programa")
    print("——————– ")
    registro = int(input("Digite sua escolha: "))

    if registro == 1:
        cadastro = str(input("Cadastre um nome: ")).lower()
        nomes.append(cadastro)
        print("Nome cadastrado.")

    elif registro == 2:
        pesquisa = str(input("Pesquise um nome: ")).lower()
        if pesquisa in nomes:
            print("Este nome está cadastrado.")
        else:
            print("Este nome não está cadastrado.")

    elif registro == 3:
        print(nomes)

    elif registro == 0:
        print("Programa finalizado.")
        break
    
    else:
        print("Escolha uma ação válida.")