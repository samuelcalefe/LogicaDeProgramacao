p1 = 0
p2 = 0

j1 = str(input("Digite nome do 1º jogador: "))
j2 = str(input("Digite nome do 2º jogador: "))

while True:
    print("----------------Placar----------------")
    print(f"{j1} = {p1} | {j2} = {p2}")
    print("--------------------------------------")
    try:
        ponto = int(input(f"Quem marcou o ponto? [1 para {j1} e 2 para {j2}]: "))
    except ValueError:
        print(f"Digite 1 para o {j1} e 2 para o {j2}.")
        continue

    if ponto == 1:
        print(f"{j1} marcou o ponto!")
        p1 += 1
    elif ponto == 2:
        print(f"{j2} marcou o ponto!")
        p2 += 1
    else:
        print(f"Digite 1 para o {j1} e 2 para o {j2}.")
        continue
    
    if p1 >= 21 and (p1 - p2) >= 2:
        print(f"{j1} venceu!")
        break
    elif p2 >= 21 and (p2 - p1) >= 2:
        print(f"{j2} venceu!")
        break