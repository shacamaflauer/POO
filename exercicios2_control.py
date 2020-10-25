from datetime import date
from exercicios2.model import Data

#inicialização das variaveis globais
x = 0
ano = 0
mes = 0
dia = 0

#estrutura para inserir os dados da data
print("Insira a data de consulta: ")

#laço para inserir ano correto, so vale para valores inteiro. string buga!
while x == 0:
    ano = int(input("Ano: "))
    if ano >= 1 and ano <= 9999:
        anoentrada = ano
        x = 1
    elif ano == 0:
        print("Não tem ano ZERO")
    else:
        date = date.today()
        anoentrada = date.year
        print(anoentrada)
        x = 1

#laço para inserir mes correto, so vale para valores inteiro. string buga!
while x == 1:
    mes = int(input("Mes: "))
    if mes >= 1 and mes <= 12:
        mesentrada = mes
        x = 2
    elif mes == 0:
        print("Não tem mes ZERO")
    else:
        date = date.today()
        mesentrada = date.month
        print(mesentrada)
        x = 2

#laço para inserir dia correto, so vale para valores inteiro. string buga!
while x == 2:
    dia = int(input("Dia: "))
    if mes == 2:
        if dia >= 1 and dia <= 29:
            diaentrada = dia
            break
        else:
            date = date.today()
            diaentrada = date.day
            print(diaentrada)
            break
    if mes != 2:
        if dia == 0:
            print("Não tem dia ZERO")
        elif dia >= 1 and dia <= 31:
            diaentrada = dia
            break
        else:
            date = date.today()
            diaentrada = date.day
            print(diaentrada)
            break

#instanciando a classe DATA, inserindo valores em string, como pedi o exercicio
data = Data(str(diaentrada), str(mesentrada), str(anoentrada))

#metodo para comparar as datas. Limite de ano 1 a 1999
data.comparar(data)

#metodo para buscar valor do dia da classe DATA instanciada
data.getDia(data)

#metodo para buscar valor do mes da classe DATA instanciada
data.getMes(data)

#metodo para buscar valor do ano da classe DATA instanciada
data.getAno(data)

#metodo para escrever o mes por extenso da classe DATA instanciada
data.mesExtenso(data.mes)

#metodo para responder se o Ano é bissextou ou nao
data.anoBissexto(data.ano)

data.clonar(data)