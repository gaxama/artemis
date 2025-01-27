import csv
from pathlib import Path
from pprint import pprint
from datetime import datetime

transactions1 = list(csv.reader(Path('transactions1.csv').open()))
transactions2 = list(csv.reader(Path('transactions2.csv').open()))

def reconcile_accounts(trsnsactions1, transactions2):
    
    # Convertendo as datas para objetos datetime
    for transacao1, transacao2 in zip(transactions1, transactions2):
        transacao1[0] = datetime.strptime(transacao1[0], '%Y-%m-%d')
        transacao2[0] = datetime.strptime(transacao2[0], '%Y-%m-%d')

    # Adicionando o valor "MISSING" na coluna de controle da segunda lista como padrão
    for transacao2 in transactions2:
        transacao2.append('MISSING')

    # Percorrendo a primeira lista
    for transacao1 in transactions1:
        # Estabelecendo uma variável para armazendar o índice do elemento da segunda lista que deve corresponder ao elemento da primeira
        indice_elemento_menor_data = None
        # Criando um contador do índice dos elementos da segunda lista
        contador = 0

        # Percorrendo a segunda lista
        for transacao2 in transactions2:
            
            # Verificando se as "colunas" de departamento, valor e beneficiário são iguais e se as datas estão a no máximo um dia de distância
            if transacao1[1:4] == transacao2[1:4] and abs((transacao1[0] - transacao2[0]).days) <= 1 and transacao2[4] == 'MISSING':
                
                # Verificando se já existe alguma correspondência a este elemento da primeira lista
                if indice_elemento_menor_data is None:
                    # Salvando o indice do elemento da segunda lista que corresponde ao elemento da primeira
                    indice_elemento_menor_data = contador

                # Procedendo caso ainda nbão haja uma correspondência
                else:
                    
                    # Verificando se o elemento da segunda lista encontrado apresenta uma data anterior ao elemento já correspondente
                    if transacao2[0] < transactions2[indice_elemento_menor_data][0]:
                        # Salvando o indice do elemento da segunda lista que corresponde ao elemento da primeira
                        indice_elemento_menor_data = contador
            
            # Aumentando 1 valor no contador do índice dos elementos da segunda lista
            contador += 1
        
        # Verificando se houve alguma correspondencia e adicionando/alterando a coluna de controle
        if indice_elemento_menor_data is None:
            transacao1.append('MISSING')

        # Procedendo caso haja uma correspondência
        else:
            transacao1.append('FOUND')
            transactions2[indice_elemento_menor_data][4] = 'FOUND'

    # Convertendo datas de volta para strings
    for transacao1, transacao2 in zip(transactions1, transactions2):
        transacao1[0] = transacao1[0].strftime('%Y-%m-%d')
        transacao2[0] = transacao2[0].strftime('%Y-%m-%d')

    return transactions1, transactions2

out1, out2 = reconcile_accounts(transactions1, transactions2)

pprint(out1)
pprint(out2)