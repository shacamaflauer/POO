from exercicios4.model import Prova, Gabarito

questoes = []
gabarito = Gabarito.respostaAluno(questoes)
prova = Prova(gabarito)
acertos = Gabarito.acertos(gabarito)
print(acertos, 'Acertos.')
nota = Gabarito.nota(gabarito)
print('Sua nota é {}'.format(nota))