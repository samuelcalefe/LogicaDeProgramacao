pesoTerra = float(input("Digite seu peso: "))
planeta = int(input("Mercúrio = 1 | Vênus = 2 | Marte = 3 | Júpiter = 4 | Saturno = 5 | Urano = 6 \nEscolha o código do seu planeta: "))

match planeta:
 case 1:
     pesoPlaneta = pesoTerra * 0.37
     print("Seu peso em Mercúrio seria", pesoPlaneta) # Calcula o peso em Mercúrio
 
 case 2:
     pesoPlaneta = pesoTerra * 0.88
     print("Seu peso em Vênus seria", pesoPlaneta) # Calcula o peso em Vênus
 
 case 3:
     pesoPlaneta = pesoTerra * 0.38
     print("Seu peso em Marte seria", pesoPlaneta) # Calcula o peso em Marte
 
 case 4:
     pesoPlaneta = pesoTerra * 2.64
     print("Seu peso em Júpiter seria", pesoPlaneta) # Calcula o peso em Júpiter
 
 case 5:
     pesoPlaneta = pesoTerra * 1.15
     print("Seu peso em Saturno seria", pesoPlaneta) # Calcula o peso em Saturno
 
 case 6:
     pesoPlaneta = pesoTerra * 1.17
     print("Seu peso em Urano seria", pesoPlaneta) # Calcula o peso em Urano 
 
 case _:
     print("Código Inválido.")