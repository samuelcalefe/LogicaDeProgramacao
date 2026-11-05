senhaDef = int(input("Defina uma senha: "))
print("Senha definida.")

senha = ("Digite a senha: ")
while senha != senhaDef:
    senha = int(input("Errado. Digite a senha: "))
    continue
else:
    print("Senha desbloqueada.")