programa {
  funcao inicio() {
    inteiro celsius, temp
    real fahrenheit, kelvin
    escreva("Digite sua temperatura em celsius: ")
    leia(celsius)
    escreva("Sua temperatura em celsius: " + celsius, "\nKelvin - 1 | Fahrenheit - 2")
    escreva("\nEscolha para qual queres converter: ")
    leia(temp)
    se(temp == 1){
      kelvin = celsius + 273.15
      escreva("Sua temperatura de Celsius para Kelvin é de " + kelvin)
    }senao se(temp == 2){
      fahrenheit = (celsius * 1.8) + 32
      escreva("Sua temperatura de Celsius para Fahrenheit é de " + fahrenheit)
    }senao{
      escreva("Inválido.")
    }
    
  }
}
