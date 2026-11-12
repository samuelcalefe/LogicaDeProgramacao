itens = 0

while True:
    print("------------------------CARDÁPIO------------------------")
    print("100 - Cachorro Quente - R$1,20  | 103 - Hamburger     - R$1,20")
    print("101 - Bauru Simples   - R$1,30  | 104 - Cheeseburger  - R$1,30")
    print("102 - Bauru Com Ovo   - R$1,50  | 105 - Refrigerante  - R$1,00")
    print("--------------------------------------------------------")

    ped = int(input("Escolha o código do item desejado (ou 0 para finalizar): "))
    while ped not in [0, 100, 101, 102, 103, 104, 105]:
        ped = int(input("Escolha um código válido: "))

    if ped == 100:
        print("Selecionou Cachorro Quente. Adicionado R$1,20 ao pedido.")
        itens += 1.20
    elif ped == 101:
        print("Selecionou Bauru Simples. Adicionado R$1,30 ao pedido.")
        itens += 1.30
    elif ped == 102:
        print("Selecionou Bauru com Ovo. Adicionado R$1,50 ao pedido.")
        itens += 1.50
    elif ped == 103:
        print("Selecionou Hamburger. Adicionado R$1,20 ao pedido.")
        itens += 1.20
    elif ped == 104:
        print("Selecionou Cheeseburger. Adicionado R$1,30 ao pedido.")
        itens += 1.30
    elif ped == 105:
        print("Selecionou Refrigerante. Adicionado R$1,00 ao pedido.")
        itens += 1

    again = str(input("Escolher outro item? [y/n]:"))
    while again not in ["y", "n"]:
        again = str(input("Digite y para sim ou n para não: "))

    if again == "n" or ped == 0:
        print(f"Pedido finalizado. Total: R${itens}")
        break
    
