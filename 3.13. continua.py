multiplos5 = 0
naoDiv10 = 0
contador = 0
contadorTotal = 0
maiorTemperatura = 0
while True:
    temperatura = float(input("Digite a temperatura (ou 999 para encerrar): "))
    contadorTotal += 1
    if temperatura == 999:
        break
    if temperatura < -50 or temperatura > 150:
        print("Temperatura inválida, tente novamente. ")
    elif temperatura >= 20 and temperatura <= 80:
        contador += 1
        if temperatura % 5 == 0:
            multiplos5 += 1
        if temperatura % 10 != 0:
            naoDiv10 += 1  
    if  temperatura >= 20 and temperatura <= 80:
        if temperatura > maiorTemperatura:
            maiorTemperatura = temperatura
    elif maiorTemperatura == 999:
        break
print(f"Quantidade de temperaturas válidas: {contador}")    
print(f"Maior temperatura válida: {maiorTemperatura}")
percentualValido = (contador / contadorTotal) * 100
print(f"Percentual válido sobre total digitado: {percentualValido}%")