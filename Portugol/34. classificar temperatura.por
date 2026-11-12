programa {
  funcao inicio() {
    inteiro temp
    escreva("Digite a temperatura: ")
    leia(temp)

    se(temp <= -1){
      escreva("Muito frio")
    }senao {}
    se(temp >= 0 e temp <= 15){
      escreva("Frio")
    }senao {}
    se(temp >= 16 e temp <= 25){
      escreva("Ameno")
    }senao {}
    se(temp >= 26 e temp <= 35){
      escreva("Quente")
    }senao {}
    se(temp >= 36){
      escreva("Muito quente")
    }

    }
    
  }