from datetime import date

class Data:

    def __init__(self, diarec, mesrec, anorec):
        self.dia = diarec
        self.mes = mesrec
        self.ano = anorec

    def comparar(self, data):
        hoje = date.today()
        hoje = str(hoje)
        ano = (hoje[0]+hoje[1]+hoje[2]+hoje[3])
        ano = int(ano)
        mes = (hoje[5]+hoje[6])
        mes = int(mes)
        dia = (hoje[8]+hoje[9])
        dia = int(dia)

        if ano > int(data.ano):
            print('A data é menor: -1')
        elif ano < int(data.ano):
            print('A data é maior: 1')
        else:
            if mes > int(data.mes):
                print('A data mes é menor: -1')
            elif mes < int(data.mes):
                print('A data mes é maior: 1')
            else:
                if dia > int(data.dia):
                    print('A data é menor: -1')
                elif dia < int(data.dia):
                    print('A data é maior: 1')
                else:
                    print('A data é igual: 0')

    def getDia(self, data):
        return print('dia:',int(data.dia))

    def getMes(self, data):
        return print('mes:',int(data.mes))

    def getAno(self, data):
        return print('ano:',int(data.ano))

    def mesExtenso(self, mes):
        meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes = int(mes)
        for n in meses:
            if n == (meses[mes - 1]):
                print('O mes é',meses[mes - 1],'!')

    def anoBissexto(self, ano):
        ano = int(ano)

        anobi = ano % 4
        if anobi == 0:
            anobi = ano / 100
            if anobi != 0:
                print('Verdadeiro, ano é bissexto!')
            else:
                print('Falso, ano não é bissexto!')
        elif anobi != 0:
            anobi = ano / 400
            if anobi != 0:
                print('Falso, ano não é bissexto!')
            elif anobi == 0:
                print('Verdadeiro, ano é bissexto!')

    def clonar (self, data):
        return print(data.dia+'/'+data.mes+'/'+data.ano)
        