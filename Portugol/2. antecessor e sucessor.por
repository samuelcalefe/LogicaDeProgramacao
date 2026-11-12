// leia um numero inteiro e mostre seu antecessor e sucessor
programa {
  funcao inicio() {
    inteiro numero, antecessor, sucessor
    escreva ("Digite um número: ")
    leia (numero)
    antecessor = numero - 1
    sucessor = numero + 1
    escreva ("O antecessor do seu número é " + antecessor, ", e o sucessor é " + sucessor)
    
  }
}
