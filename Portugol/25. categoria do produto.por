programa {
  funcao inicio() {
    real valorProduto
    escreva("Digite o valor do produto: ")
    leia(valorProduto)
    se(valorProduto >= 1 e valorProduto <= 50){
      escreva("Produto econômico.")
    }senao se(valorProduto >= 51 e valorProduto <= 150){
      escreva("Produto médio.")
    }senao se(valorProduto >= 151){
      escreva("Produto premium.")
    }senao{
      escreva("Inválido.")
    }

    
  }
}
