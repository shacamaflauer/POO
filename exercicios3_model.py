class Voo:

    def __init__(self, numerovoo, data):
        self.numerovoo = numerovoo
        self.data = data

    def proximoLivre(assentoescolhido):
        assentoescolhido = assentoescolhido+1
        return assentoescolhido

    def verificaOcupado(assento, assentoescolhido):
        if assento[assentoescolhido-1] == False:
            #assento[assentoescolhido-1] = True
            print('Falso = Assento {} disponivel.\n'.format(assentoescolhido))
            x = int(input('Você deseja ocupar o assento? (1)Sim || (2)Não'))
            if x == 1:
                Voo.ocupaAssento(assento, assentoescolhido)
            else:
                print('Nenhuma alteração...')
        else:
            print('Verdadeiro = Ocupado!')
            x = int(input('Você deseja liberar o assento? (1)Sim || (2)Não'))
            if x == 1:
                Voo.liberaAssento(assento, assentoescolhido)
            else:
                assentoescolhido = Voo.proximoLivre(assentoescolhido)
                print('Proximo assento...')
                Voo.verificaOcupado(assento, assentoescolhido)

    def ocupaAssento(assento, assentoescolhido):
        if assento[assentoescolhido - 1] == False:
            assento[assentoescolhido - 1] = True
            print('Assento {} escolhido.\n'.format(assentoescolhido))
        else:
            print('Verdadeiro = Ocupado!')

    def liberaAssento(assento, assentoescolhido):
        if assento[assentoescolhido - 1] == True:
            assento[assentoescolhido - 1] = False
            print('Assento {} liberado.\n'.format(assentoescolhido))
        else:
            print('Falso = Disponivel!')

    def contaAssento(assentos):
        for n in range(100):
            if assentos[n] == False:
                ocupados = assentos.count(False)
        return print('Tem {} vagos.\n'.format(ocupados))

    def getVoo(voo):
        print('Numero do voo:', voo.numerovoo)

    def getData(voo):
        print('Data do voo:', voo.data.dia+'/'+voo.data.mes+'/'+voo.data.ano)

    def clonar(voo):
        clone = [voo.numerovoo, voo.data.dia, voo.data.mes, voo.data.ano]
        print(clone)