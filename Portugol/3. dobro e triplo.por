// ler um numero e mostrar o dobro e o triplo dele
programa {
  funcao inicio() {
    inteiro numero, dobro, triplo
    escreva ("Digite um número: ")
    leia (numero)
    dobro = numero * 2
    triplo = numero * 3
    escreva ("O dobro do número é " + dobro, ", e o triplo é " + triplo)
  }
}
