// calculadora
programa {
  funcao inicio() {
    inteiro operacao
    real valor1, valor2, valorFinal
    escreva ("Digite o valor 1: ")
    leia (valor1)
    escreva ("Digite o valor 2: ")
    leia (valor2)
    escreva ("Adição = 1 | Subtração = 2 | Multiplicação = 3 | Divisão = 4\nEscolha a operação: ")
    leia(operacao)
    se(operacao == 1){
      escreva (valor1 + valor2)
    }senao{}
    se(operacao == 2){
      escreva (valor1 - valor2)
    }senao{}
    se(operacao == 3){
      escreva (valor1 * valor2)
    }senao{}
    se(operacao == 4){
      escreva (valor1 / valor2)
    }senao{}
    se(operacao >= 5 ou operacao <= 0){
      escreva ("Inválido.")
    }

    
  }
}
