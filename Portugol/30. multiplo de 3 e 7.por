programa {
  funcao inicio() {
    inteiro numero
    escreva("Digite um número: ")
    leia(numero)
    se (numero % 7 == 0 e numero % 3 == 0){
      escreva (numero, " é múltiplo de 7 e 3.")
    }senao{
      escreva (numero, " não é múltiplo de 7 e 3.")
    }
    
  }
}
