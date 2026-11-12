anos = 0
pop_A = 90
pop_B = 140

print("------------------------------------------------------------------------------------------")
print("População A tem 90 milhões de habitantes e População B tem 140 milhões de habitantes.")
while True:
    if pop_B > pop_A:
        pop_A *= 1.035
        pop_B *= 1.01
        anos += 1
    else:
        print(f"População A passará de B em {anos} anos. População A terá {pop_A} milhões e B terá {pop_B} milhões.")
        print("------------------------------------------------------------------------------------------")
        break
