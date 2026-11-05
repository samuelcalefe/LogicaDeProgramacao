# Escolhendo o dia da semana
print("1 - Domingo | 2 - Segunda | 3 - Terça | 4 - Quarta | 5 - Quinta | 6 - Sexta | 7 - Sábado")
dia = int(input("Escolha o dia da semana: "))

# Exibindo os turnos
match dia:
  case 1:
     print("Sem trabalho")

  case 7:
     print("Turno reduzido")

  case 2 | 3 | 4 | 5 | 6:
     print("Turno normal")

  case _:
     print("Inválido")