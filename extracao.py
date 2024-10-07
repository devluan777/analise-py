import os
import time
import json
from random import random
from datetime import datetime
import requests

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados?formato=json'

def extrair_dados():
    for _ in range(0, 10):
        data_e_hora = datetime.now()
        data = datetime.strftime(data_e_hora, '%Y/%m/%d')
        hora = datetime.strftime(data_e_hora, '%H:%M:%S')

        for _ in range(3):  # Tentar até 3 vezes
            try:
                response = requests.get(URL)
                response.raise_for_status()
                break  # Se a solicitação for bem-sucedida, sair do loop
            except requests.RequestException as exc:
                print("Erro ao obter dados, tentando novamente...")
                time.sleep(5)  # Esperar 5 segundos antes de tentar novamente
        else:
            print("Erro, parando a execução.")
            raise Exception("Não foi possível obter os dados após várias tentativas.")

        dado = json.loads(response.text)
        cdi = float(dado[-1]['valor']) + (random() - 0.5)

        if not os.path.exists('./taxa-cdi.csv'):
            with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
                fp.write('data,hora,taxa\n')

        with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
            fp.write(f'{data},{hora},{cdi}\n')

        time.sleep(2 + (random() - 0.5))

    print("Sucesso")

if __name__ == "__main__":
    extrair_dados()
