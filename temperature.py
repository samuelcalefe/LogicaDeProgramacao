temp = int(input("Digite sua temperatura: "))
if temp < 18:
   print("Temperatura baixa")
elif temp >= 18 and temp <= 25:
   print("Temperatura média")
else:
   print("Temperatura alta")