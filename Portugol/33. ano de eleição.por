programa {
  funcao inicio() {
    inteiro ano, idade
    escreva("Digite o seu ano de nascência: ")
    leia(ano)
    idade = 2026 - ano
    se(idade <= 15){
      escreva("Sua idade é de " + idade, " anos, então não pode votar.")
    }senao se(idade >= 16 e idade <= 17){
      escreva("Sua idade é de " + idade, " anos. Podes votar opcionalmente.")
    }senao se(idade >= 18 e idade <= 90){
      escreva("Sua idade é de " + idade, " anos. Deves votar.")
    }
    
  }
}
