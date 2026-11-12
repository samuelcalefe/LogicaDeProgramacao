// leia a idade da pessoa e se ela esta acompanhada. deixe-a entrar se for maior de 18 ou pelo menos 16 e tiver acompanhamento
programa {
  funcao inicio() {
    inteiro idade, acompanhada
    escreva ("Digite a sua idade: ")
    leia (idade)
    se(idade >= 18 e (idade >= 16)){
      escreva ("Permitida")
    } senao {
    escreva ("Você está acompanhado(a)? \n1 = sim 2 = não \nResposta: ")
    leia (acompanhada)
    se(acompanhada == 1){
      escreva ("Permitida")
    } senao {
      escreva ("Negado")
    }
      
    }
    
  }
}
