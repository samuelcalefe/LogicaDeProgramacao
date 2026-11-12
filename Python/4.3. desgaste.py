desgaste = 0
ciclo = 0

while desgaste < 500:
    ciclo += 1
    if ciclo > 70:
        desgaste += 10
    else:
        desgaste += 7
    if desgaste >= 500:
        print("------------------------------")
        print(f"Desgaste final: {desgaste}")
        print(f"Ciclos: {ciclo}")
        print("------------------------------")
        break