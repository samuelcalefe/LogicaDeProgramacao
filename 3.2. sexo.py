homem = 0
mulher = 0

print("--------------------------------")
for i in range (56):
    nome = input("Digite seu nome: ")
    sexo = input("Digite seu sexo [homem/mulher]: ").lower()
    while sexo not in ["homem", "mulher"]:
        sexo = input("Digite homem ou mulher: ").lower()

    if sexo == "homem":
        print(f"{nome} é um homem.")
        homem += 1
    elif sexo == "mulher":
        print(f"{nome} é uma mulher.")
        mulher += 1

print(f"Dentre as {i} pessoas, existem {homem} homens e {mulher} mulheres.")