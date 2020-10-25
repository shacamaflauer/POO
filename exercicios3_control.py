from datetime import date
from exercicios2.model import Data
from exercicios3.model import Voo

#inicialização das variaveis globais
x = 0
ano = 0
mes = 0
dia = 0
print('Inserir os dados do Voo: ex.: Data(22/10/2020)')
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

numerovoo = input('Inserir o numero do Voo. Valor numerico inteiro: ')
data = Data(str(diaentrada), str(mesentrada), str(anoentrada))
voo = Voo(numerovoo, data)
print('\nNumero do Voo: '+voo.numerovoo,'--','Data do Voo: '+data.dia+'/'+data.mes+'/'+data.ano)
print('\n')


assento = []
n = ''
x = 0
#criar lista de assentos livres
for n in range(100):
    assento.append(False)
#laço de repetição do VOO
while x == 0:
    print('Escolha a opção desejada. \n'
          '(1)Verificar Assento Ocupado\n'
          '(2)Ocupar Assento\n'
          '(3)Contar Assento\n'
          '(4)Buscar Numero do Voo\n'
          '(5)Buscar Data do voo\n'
          '(6)Clonar Voo\n'
          '(7)Sair\n')
    menu = int(input('Opção desejada? '))

    if menu == 1:
        assentoescolhido = int(input('Digite o assento: '))
        Voo.verificaOcupado(assento, assentoescolhido)

    elif menu == 2:
        assentoescolhido = int(input('Digite o assento: '))
        Voo.ocupaAssento(assento, assentoescolhido)

    elif menu == 3:
        Voo.contaAssento(assento)

    elif menu == 4:
        Voo.getVoo(voo)

    elif menu == 5:
        Voo.getData(voo)

    elif menu == 6:
        Voo.clonar(voo)

    else:
        print('Você saiu.')
        break