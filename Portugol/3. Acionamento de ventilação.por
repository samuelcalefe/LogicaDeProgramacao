programa {
  funcao inicio() {
    inteiro pessoas, temp
    escreva("Digite a temperatura: ")
    leia(temp)
    escreva("1 - Sim | 0 - Não \nHá pessoas no ambiente?: ")
    leia(pessoas)
    se(pessoas >= 2){
      escreva("Digite 1 para sim ou 0 para não. ")
    }senao{}
    se(temp >= 28 e pessoas == 1){
      escreva("Ventilador ligado.")
    }senao{
      escreva("Ventilador desligado.")
    }
    
  }
}
