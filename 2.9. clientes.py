for clientes in range (150):
    nome = str(input("Escreva o nome do cliente: "))
    compras = float(input("Escreva o valor das compras dele: "))

    if compras < 500000:
        desc10 = compras - (compras * 0.10)
        print(f"O cliente {nome} recebeu um bônus de 10%.")
        print(f"R${compras} foi para R${desc10}")
        
    elif compras >= 500000:
        desc15 = compras - (compras * 0.15)
        print(f"O cliente {nome} recebeu um bônus de 15%.")
        print(f"R${compras} foi para R${desc15}")
        