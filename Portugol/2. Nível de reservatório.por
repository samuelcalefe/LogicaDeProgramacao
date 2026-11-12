programa {
  funcao inicio() {
    real porcentagem
    escreva("Informe o porcentual: ")
    leia(porcentagem)
    se(porcentagem <= -1){
      escreva("Inválido.")
    }senao se(porcentagem >= 0 e porcentagem < 20){
      escreva("Nível crítico.")
    }senao se(porcentagem >= 21 e porcentagem < 80){
      escreva("Nível adequado.")
      }senao se(porcentagem >= 80 e porcentagem <= 100){
        escreva("Nível alto")
      }senao{
        escreva("Inválido.")
      }
    }
    
  }

