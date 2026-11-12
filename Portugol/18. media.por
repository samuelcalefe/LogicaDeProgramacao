// calcular a média entre três notas
programa {
  funcao inicio() {
    real nota1, nota2, nota3, media
    escreva ("Digite a primeira nota: ")
    leia (nota1)
    escreva ("Digite a segunda nota: ")
    leia (nota2)
    escreva ("Digite a terceira nota: ")
    leia (nota3)
    media = (nota1 + nota2 + nota3) / 3
    se(media >= 7 e media <= 10){
      escreva ("Aprovado com uma média de " + media)
    }senao se(media >=0 e media <=6){
      escreva("Reprovado com uma média de " + media)
    }
}
}
