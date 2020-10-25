from exercicios1.model import Aluno

notas = []
nome = input('nome: ')
matricula = input('matricula: ')
x = 1
i = 0
while x == 1: # laço de repetição para inserir as notas
    if i < 3:
        nota = float(input("Nota[{}]".format(i+1)))
        if nota <= 10 and nota >= 0: # desvio de fluxo para verificar se as notas são corretas
            notas.append(nota)
            print(notas)
            print('')
            i = 1 + i
        else:
            print('nota invalida!')
    else:
            break

aluno = Aluno(nome, matricula) #instancia a classe Aluno e recebe o valres das variaveis de entrada de dados

mediaFinal = Aluno.mediaFinal(notas[0], notas[1], notas[2]) # metodo da classe Aluno que verifica a media final

resultadofinal = Aluno.situacao(mediaFinal, aluno.nome) # metodo para mostrar a situação do aluno

examefinal = Aluno.exameFinal(mediaFinal) # metodo para saber nota do exame final

print(f'Voce precisa tirar {examefinal:.2f} no exame final!')
