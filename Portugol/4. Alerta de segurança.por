programa {
  funcao inicio() {
    inteiro estado, sistema
    escreva ("1 - Aberta | 2 - Fechada \nEstado da porta: ")
    leia(estado)
    se(estado >= 3){
      escreva("Valor inválido. \nDigite 1 para Aberta e 2 para Fechada.")
    }senao{
      escreva("1 - Acionado | 2 - Desligado \nO sistema de segurança está: ")
      leia(sistema)
      se(sistema >= 3){
        escreva("Valor inválido. Digite 1 se estiver Acionado e 2 se estiver Desligado.")
      }senao{
        se(estado == 1 e sistema == 1){
          escreva("!! ALERTA DE SEGURANÇA !!")
        }senao{
          escreva("Situação normal")
        }
      }
    }
    
  }
}
