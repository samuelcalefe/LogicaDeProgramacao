meta = 500
cap = 50
chegada = 48
filas = [0, 0, 0, 0, 0]
estresse = [0, 0, 0, 0, 0]
prod = 0
ciclos = 0
falha = 0
limite = 0.9 * cap

while prod < meta and falha == 0:
    ciclos += 1
    filas[0] += chegada

    for i in range(5):
        if filas[i] < cap:
            qtd = filas[i]
        else:
            qtd = cap

        filas[i] -= qtd

        if i == 4:
            prod += qtd
        else:
            filas[i + 1] += qtd

        if qtd > limite:
            estresse[i] += 1
            if estresse[i] >= 5:
                falha = i + 1
                break
        else:
            estresse[i] = 0

print("--------------------------------------------")
print(f"Produção total: {prod} peças")
if falha > 0:
    print(f"Estação que falhou: Estação {falha}")
else:
    print("Estação que falhou: Nenhuma")
print(f"Ciclos executados: {ciclos}")
print("--------------------------------------------")