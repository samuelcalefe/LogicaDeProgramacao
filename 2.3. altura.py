anos = 0
altura_ze = 1.10
altura_joao = 1.50

print("------------------------------------------------------------------------------------------")
print("João tem 1.50cm de altura e Zé tem 1.10cm de altura.")
while True:
    if altura_joao > altura_ze:
        altura_ze += 0.03
        altura_joao += 0.01
        anos += 1
    else:
        print(f"Zé passará de João daqui a {anos} anos; Zé terá {altura_ze}0cm e João terá {altura_joao}0cm.")
        print("------------------------------------------------------------------------------------------")
        break
