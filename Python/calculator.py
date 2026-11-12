# Inserindo os valores
print("Adição -> + | Subtração -> - | Multiplicação -> * | Divisão -> /")
num1 = float(input("1º Valor: "))
opera = (input("Operação: "))
num2 = float(input("2º Valor: "))

# Calculando
if opera == "+":
    addition = num1 + num2
    print("Resultado:", addition)

elif opera == "-":
    subtraction = num1 - num2
    print("Resultado:", subtraction)

elif opera == "*":
    multiplication = num1 * num2
    print("Resultado:", multiplication)

elif opera == "/":
    division = num1 / num2
    print("Resultado:", division)

else:
    print("Inválido")