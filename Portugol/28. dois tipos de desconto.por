programa {
  funcao inicio() {
    real valorCompra, valorTotal
    escreva ("Digite o valor da compra: ")
    leia (valorCompra)
    se(valorCompra <= 100){
     valorTotal = valorCompra - (valorCompra * 0.05)
     escreva("Você recebeu um desconto de 5%. \nSua compra foi de R$" + valorCompra, " para R$" + valorTotal)
    }senao se(valorCompra >= 100){
      valorTotal = valorCompra - (valorCompra * 0.1)
      escreva("Você recebeu um desconto de 10%. \nSua compra foi de R$" + valorCompra, " para R$" + valorTotal)
    } senao se(valorCompra <= -1){
      escreva("Inválido.")
    }
    }

    
  }

