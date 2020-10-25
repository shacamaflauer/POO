class Prova:

    def __init__(self, gabarito):
        self.gabarito = gabarito

class Gabarito:

    def __init__(self, questao):
        self.questao = questao

    def respostaAluno(prova):

        for n in range(15):
            #"""alterar tamanho do RANGE para estipular quantidade de perguntas na prova,
            # deve-se mudar também os valores de cada alternativa mais embaixo se mudar quantidade de questoes
            print('Questão {}, responda: (A, B, C, D, E)'.format(n + 1))
            #não ha restrições de entrada de alternativa, então se preencher o caracter incorreto, a questão sera anulada
            questao = input('Alternativa: ')
            print('')
            prova.append(questao)
        return prova

    def acertos(gabarito):
        #Lista abaixo é das questoes corretas da prova(alterar conforme as alternativas corretas)
        respostas = ['a', 'b', 'c','d', 'e', 'a','b', 'c', 'd', 'e','a','b', 'c', 'd', 'e']
        acertos = 0
        for n in range(15):
            if gabarito[n] == respostas[n]:
                acertos = acertos + 1
        return acertos

    def nota(gabarito):
        #Lista abaixo é das questoes corretas da prova(alterar conforme as alternativas corretas)
        respostas = ['a', 'b', 'c','d', 'e', 'a','b', 'c', 'd', 'e','a','b', 'c', 'd', 'e']
        nota = 0
        for n in range(15):
            if gabarito[n] == respostas[n]:
                if n < 10:
                    # """0.50 é o valor de cada questão ate a de numero 10, de uma prova com 15 questoes
                    nota = nota + 0.50
                if n >= 10:
                    # """1.0 é o valor de cada questã da prova, do numero 11 ate 15 da prova de 15 questoes
                    nota = nota + 1
        return nota
        
