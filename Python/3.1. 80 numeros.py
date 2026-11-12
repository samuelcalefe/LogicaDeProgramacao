entre = 0

print("------------------------------------")
for i in range (80):
    i = float(input(f"Digite o {i}º número: "))
    if i >= 10 and i <= 150:
        entre += 1

print(f"Entre os {i} números digitados, {entre} foram entre 10 e 150.")