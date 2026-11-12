// algoritmo que calcule e exiba o valor do desconto baseado no tipo de combustivel e o valor a ser pago pelo cliente
programa {
  funcao inicio() {
    real combustivel, valorFinal, valor
    escreva ("Digite o valor do seu veículo: ")
    leia (valor)
    escreva ("Álcool = 1 | Gasolina = 2 | Díesel = 3 \nEscolha qual o tipo de combustível: ")
    leia (combustivel)
    se(combustivel <= 0){
      escreva ("O valor à ser pago é de " + valor, ", sem desconto.")
    }senao{}
    se(combustivel == 1){
      valorFinal = valor - (valor * 0.25)
      escreva ("O valor à ser pago é de " + valorFinal, ", com desconto de 25%.")
    }senao{}
    se(combustivel == 2){
      valorFinal = valor - (valor * 0.21)
      escreva ("O valor à ser pago é de " + valorFinal, ", com desconto de 21%.")
    }senao{}
    se(combustivel == 3){
      valorFinal = valor - (valor * 0.14)
      escreva ("O valor à ser pago é de " + valorFinal, ", com desconto de 14%.")
    }senao{}
    se(combustivel >= 4){
      escreva ("O valor à ser pago é de " + valor, ", sem desconto.")
    }
  }
}
