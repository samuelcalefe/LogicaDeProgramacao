programa {
  funcao inicio() {
    inteiro temperatura
    escreva("Digite a temperatura: ")
    leia(temperatura)
    se(temperatura < 18){
      escreva("Temperatura baixa")
    }senao{
      se(temperatura >= 18 e temperatura <= 25){
        escreva("Temperatura média")
      }senao{
        se(temperatura > 25){
          escreva("Temperatura alta")
        }
      }
    }
    
  }
}
