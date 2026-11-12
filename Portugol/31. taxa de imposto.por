programa {
  funcao inicio() {
    real salario, imposto
    escreva("Digite o seu salário: ")
    leia (salario)
    se(salario >=0 e salario <= 1000){
      escreva("Seu salário total é de " + salario, " sem impostos.")
    }senao{}
    se(salario >= 1001 e salario <= 3000){
          imposto = salario - (salario * 0.1)
          escreva("Seu salário total é de R$" + imposto, " com 10% de impostos.")
    }senao{}
    se(salario >= 3001 e salario <= 5000){
      imposto = salario - (salario * 0.15)
      escreva("Seu salário total é de R$" + imposto, " com 15% de impostos.")
    }senao{}
    se(salario >= 5001){
      imposto = salario - (salario * 0.20)
      escreva("Seu salário total é de R$" + imposto, " com 20% de impostos.")
    }

    
  }
}
