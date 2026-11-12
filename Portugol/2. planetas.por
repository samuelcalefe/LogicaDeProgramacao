// programa que le o seu peso na terra e calcula qual seria seu peso em outro planeta
programa {
  funcao inicio() {
    inteiro pesoTerra, planeta
    real pesoPlaneta
    escreva ("Digite o seu peso: ")
    leia (pesoTerra)
    escreva ("mercurio = 1, venus = 2, marte = 3, jupiter = 4, saturno = 5, urano = 6 \nEscolha o código do seu planeta: ")
    leia (planeta)
    se(planeta <= 0){
     escreva ("Inválido")
    }senao{}
    se(planeta == 1){
      pesoPlaneta = (pesoTerra / 10) * 0.37
      escreva ("Seu peso em mercúrio seria " + pesoPlaneta)
    }senao{}
    se(planeta == 2){
      pesoPlaneta = (pesoTerra / 10) * 0.88
      escreva ("Seu peso em vênus seria " + pesoPlaneta)
    }senao{}
    se(planeta == 3){
      pesoPlaneta = (pesoTerra / 10) * 0.38
      escreva ("Seu peso em marte seria " + pesoPlaneta)
    }senao{}
    se(planeta == 4){
      pesoPlaneta = (pesoTerra / 10) * 2.64
      escreva ("Seu peso em júpiter seria " + pesoPlaneta)
    }senao{}
    se(planeta == 5){
      pesoPlaneta = (pesoTerra / 10) * 1.15
      escreva ("Seu peso em saturno seria " + pesoPlaneta)
    }senao{}
    se(planeta == 6){
      pesoPlaneta = (pesoTerra / 10) * 1.17
      escreva ("Seu peso em urano seria " + pesoPlaneta)
    }senao{}
    se(planeta >= 7){
      escreva ("Inválido")
    }


    
  }
}
