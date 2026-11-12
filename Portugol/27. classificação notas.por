// programa que imprime o conceito de um aluno dada a sua nota
programa {
  funcao inicio() {
    real nota
    escreva ("Digite a nota do aluno: ")
    leia (nota)
    se(nota <= 0){
      escreva ("Inválido")
    }senao{}
    se(nota >= 0.0 e nota <= 2.9){
      escreva ("Classificação E")
    }senao{
      se(nota >= 3.0 e nota <= 4.9){
        escreva ("Classificação D")
      }senao{
        se(nota >= 5.0 e nota <= 6.9){
          escreva ("Classificação C")
        }
      }
    }
    se(nota >= 7.0 e nota <= 8.9){
      escreva ("Classificação B")
    }senao{
      se(nota >= 9.0 e nota <= 10){
        escreva ("Classificação A")
      }senao{
        se(nota >= 11)
        escreva ("Inválido")
      }
    }
    }
    }
    
    
    
  
