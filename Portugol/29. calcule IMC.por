programa {
  funcao inicio() {
    real peso, altura, imc
    escreva("Digite o seu peso: ")
    leia(peso)
    escreva("Digite a sua altura: ")
    leia(altura)
    imc = peso / (altura * altura)

    se(imc <= 18.4){
      escreva("Abaixo do peso: " + imc)
    }senao {}
    se(imc >= 18.5 e imc <= 24.9){
      escreva("Peso normal: " + imc)
    }senao {}
    se(imc >= 25.0 e imc >= 29.9){
      escreva("Sobrepeso: " + imc)
    }senao {}
    se(imc >= 30.0){
      escreva("Obeso: " + imc)
    }

    }
    
  }
}
