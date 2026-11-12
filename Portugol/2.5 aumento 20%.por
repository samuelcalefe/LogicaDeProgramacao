// calcule o aumento de 20% no preço dos itens de uma loja e mostre a media
programa {
  funcao inicio() {
    inteiro preco, precoNovo, codigo, media
    escreva ("Código: ")
    leia (codigo)
    escreva ("Digite o preço: ")
    leia (preco)
    precoNovo = (preco * 0.20) + preco
    media = (preco + precoNovo) / 2
    escreva ("O produto com código " + codigo, " teve o preço reajustado para " + precoNovo, "\nA média dos valores é de " + media, ".")
    
  }
}
