print("---------------------------------------------")
valorCarro = float(input("Digite o valor do carro: "))
vista = valorCarro - (valorCarro * 0.20)

# valores de parcelas
parc6 = (valorCarro + (valorCarro * 0.03)) / 6
parc12 = (valorCarro + (valorCarro * 0.06)) / 12
parc18 = (valorCarro + (valorCarro * 0.09)) / 18
parc24 = (valorCarro + (valorCarro * 0.12)) / 24
parc30 = (valorCarro + (valorCarro * 0.15)) / 30
parc36 = (valorCarro + (valorCarro * 0.18)) / 36
parc42 = (valorCarro + (valorCarro * 0.21)) / 42
parc48 = (valorCarro + (valorCarro * 0.24)) / 48
parc54 = (valorCarro + (valorCarro * 0.27)) / 54
parc60 = (valorCarro + (valorCarro * 0.30)) / 60

print("---------------------------------------------")

print("Opções de pagamento:")
print("À vista:")
print(f"R${vista} (20% off)")

print("---------------------------------------------")

print("Parcelas:")
print(f"6x vezes: R${parc6} \n12x vezes: R${parc12} \n18x vezes: R${parc18}")
print(f"\n24x vezes: R${parc24} \n30x vezes: R${parc30} \n36x vezes: R${parc36}")
print(f"\n42x vezes: R${parc42} \n48x vezes: R${parc48} \n54x vezes: R${parc54} \n60x vezes: R${parc60}")

