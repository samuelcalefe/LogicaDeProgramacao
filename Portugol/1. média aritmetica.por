// leia tres notas e calcule a media
programa {
  funcao inicio() {
    inteiro media, nota1, nota2, nota3
    escreva ("Digite a primeira nota: ")
    leia (nota1)
    escreva ("Digite a segunda nota: ")
    leia (nota2)
    escreva ("Digite a terceira nota: ")
    leia (nota3)
    media = (nota1 + nota2 + nota3) / 3
    escreva ("Sua média é: " + media)
  }
}
