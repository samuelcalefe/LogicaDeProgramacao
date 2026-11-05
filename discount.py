valor = float(input("Digite o valor do veículo: "))
print("1 - Álcool | 2 - Gasolina | 3 - Díesel")
combustivel = int(input("\nEscolha seu combustível: "))

match combustivel:
 case 1:
     # Escolheu Álcool
     desconto = valor - (valor * 0.25)
     print("Você recebeu um desconto de 25%. O valor à ser pago agora é", desconto)

 case 2: 
     # Escolheu Gasolina
     desconto = valor - (valor * 0.21)
     print("Você recebeu um desconto de 21%. O valor à ser pago agora é", desconto)

 case 3:
     # Escolheu Díesel
     desconto = valor - (valor * 0.14)
     print("Você recebeu um desconto de 14%. O valor à ser pago agora é", desconto)
 
 case _:
     # Inseriu um valor inválido
     print("Valor de combustível inválido; Sem desconto. O valor à ser pago é", valor)