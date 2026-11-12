programa {
  funcao inicio() {
    inteiro idade
    escreva("Digite a sua idade: ")
    leia (idade)
    se(idade >= 1 e idade <= 17){
      escreva("Acesso negado.")
    }senao se(idade >=18 e idade <= 90){
      escreva ("Acesso concedido.")
    }senao escreva("ta morto ja")
    
  }
}
