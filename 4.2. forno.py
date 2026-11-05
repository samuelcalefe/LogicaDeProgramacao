ciclos = 0
temperatura = int(input("Informe a temperatura: "))

while temperatura < 1000:
    ciclos += 1
    if temperatura < 800:
        temperatura += 50
    else:
        temperatura += 20

print("---------------------------------")
print(f"Temperatura final: {temperatura}")
print(f"Ciclos: {ciclos}")
print("---------------------------------")
        