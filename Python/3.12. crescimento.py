A = int(input("Digite a população inicial de A: "))
B = int(input("Digite a população inicial de B: "))
anos = 0
while A <= B:
    A += A * 0.03
    B += B * 0.015
    anos += 1
    if anos % 5 == 0:
        A -= A * 0.07
        B -= B * 0.07

print(f"A ultrapassa B em {anos} anos.")
