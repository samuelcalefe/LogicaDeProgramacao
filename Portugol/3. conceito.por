// programa que imprime o conceito de um aluno dada a sua nota
programa {
  funcao inicio() {
    inteiro nota
    escreva ("Digite a nota do aluno: ")
    leia (nota)
    se(nota <= 0){
      escreva ("Inválido")
    }senao{}
    se(nota >= 1 e nota <= 3){
      escreva ("Conceito E")
    }senao{
      se(nota >= 3 e nota <= 5){
        escreva ("Conceito D")
      }senao{
        se(nota >= 6 e nota <= 7){
          escreva ("Conceito C")
        }
      }
    }
    se(nota >= 8 e nota <= 9){
      escreva ("Conceito B")
    }senao{
      se(nota == 10){
        escreva ("Conceito A")
      }senao{
        se(nota >= 11)
        escreva ("Inválido")
      }
    }
    }
    }
    
    
    
  
