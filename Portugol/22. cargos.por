programa {
  funcao inicio() {
    cadeia nome
    inteiro cargo
    escreva("Digite o seu nome: ")
    leia(nome)
    escreva("1 - Funcionario | 2 - Gerente | 3 - Admin \nDigite o número correspondente à sua função: ")
    leia(cargo)

    escolha(cargo)
    {
      caso 1:
      escreva("Bem vindo, " + nome, "! Você é um funcionário. \nPermissões restritas.")
      pare
      caso 2:
      escreva("Bem vindo, " + nome, "! Você é um gerente. \nPermissões: Gerenciar usuários")
      pare
      caso 3:
      escreva("Bem vindo, " + nome, "! Você é um administrador. \nPermissões completas.")
      pare
      caso contrario:
      escreva("Função inválida.")
      pare

    }
  }
}