from iqoptionapi.stable_api import IQ_Option
import time, json
from datetime import datetime
from dateutil import tz

API = IQ_Option('fernandogomes3991@outlook.com', '92864692')
API.connect()
API.change_balance('PRACTICE')  # PRACTICE / REAL

while True:
    if API.check_connect() == False:
        print('Erro ao se conectar')
        API.connect()
    else:
        print('###CONECTADO COM SUCESSO')
        print('#'*25)
        print(' ')
        print('....SEJA BEM VINDO.....')
        print(' ')
        break

    time.sleep(1)
def timestamp_converter(x,_format = '%Y.%m.%d %H:%M'):
    hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime(_format),_format)
    hora = hora.replace(tzinfo=tz.gettz('GMT'))


    return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-9]
## Pegar MAIS 1000 velas #########################
dia = 0
dias_vela = 0
moedas = ('AUDCAD','AUDJPY','AUDNZD','AUDCHF','AUDJPY','AUDUSD','EURAUD','EURUSD','EURCAD','EURNZD','EURGBP',
          'EURJPY','GBPUSD','GBPJPY','GBPCAD','GBPNZD','GBPCHF','GBPAUD','NZDUSD','USDCAD','USDJPY','USDCHF',
          'CADJPY','CADCHF','CHFJPY','USDNOK','AUDCAD-OTC')
time_ = ('M1,M5')
while True:
    par = (input('---DIGITE O PAR DE MOEDA: ').upper())
    if par in moedas:
        break
while True:
    dias_ = int(input('---QUANTOS DIAS DESEJA BUSCAR: '))
    if dias_ >= 1:
        dias = dias_
        #dias_vela = dias_ * 288
        break
while True:
    tempo_grafico = input('---QUAL TIME DESEJA M1/M5: ').upper()
    escolha = tempo_grafico
    if tempo_grafico in time_:
        if tempo_grafico == 'M1':
            tempo_grafico = 60
            break
        if tempo_grafico == 'M5':
            tempo_grafico = 300
            break

total = []
tempo = time.time()
for i in range(dias):
	X = API.get_candles(par, tempo_grafico, 1000, tempo)
	total = X+total
	tempo = int(X[0]['from'])-1

for velas in total:
    fim = (str(timestamp_converter(velas['from'])) + ',' + str(velas['open']) + ',' + str(velas['max']) + ',' + str(velas['min']) + ',' + str(velas['close']))
    open(str('arquivo') + '_'+ escolha + '.csv', 'a').write(fim+'\n')
    print(str(timestamp_converter(velas['from'])) + ',' + str(velas['open']) + ',' + str(velas['max']) + ',' + str(velas['min']) + ',' + str(velas['close']))
