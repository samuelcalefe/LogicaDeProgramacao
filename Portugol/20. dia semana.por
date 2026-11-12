// leia o dia da semana de 1 a 7
programa {
  funcao inicio() {
    inteiro dia
    escreva("Digite o dia da semana: ")
    leia(dia)
    se(dia <= 0){
      escreva ("Inválido.")
    }se(dia == 1){
      escreva ("Você escolheu Domingo.")
    }senao{
      se(dia == 2){
        escreva ("Você escolheu Segunda.")
      }
    }se(dia == 3){
      escreva ("Você escolheu Terça.")
    }senao{
      se(dia == 4){
        escreva ("Você escolheu Quarta.")
      }senao{
        se(dia == 5){
          escreva ("Você escolheu Quinta.")
        }
      }
    }
    se(dia == 6){
      escreva ("Você escolheu Sexta.")
    }senao{
      se(dia == 7){
        escreva ("Você escolheu Sábado.")
      }senao{
        se(dia >= 8){
          escreva ("Inválido.")
        }
      }
    }
  }
}

    