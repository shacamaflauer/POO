class Aluno:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def mediaFinal(prova1, prova2, trabalho1):
        mediafinal = ((prova1 * 0.30) + (prova2 * 0.30) + (trabalho1 * 0.20)) / 0.80
        return mediafinal

    def exameFinal(mediaFinal):
        return (10 - mediaFinal)

    def situacao(mediafinal, nome):
        if mediafinal >= 7:
            print(nome+" = 0")
        else:
            print("exame!")
            print(nome+" = 1 // nota: ", mediafinal)
