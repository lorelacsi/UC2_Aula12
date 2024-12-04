import pandas as pd
import polars as pl
from datetime import datetime
import gc # garbage collector
import os

try:
    ENDEREÇO_DADOS = r'./dados/'

    # hora de inicio
    hora_import = datetime.now()

    lista_arquivos = []

    lista_arquivos = os.listdir(ENDEREÇO_DADOS)

    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    for arquivo in lista_arquivos:
        print(f'Processando arquivo {arquivo}')

        df = pl.read_csv(ENDEREÇO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        if 'df_bolsa_familia' in locals():
            df_bolsa_familia = pl.concat([df_bolsa_familia,df])
        else:
            df_bolsa_familia = df

    print(df.head())

    del df

    gc.collect()

    hora_impressao = datetime.now()

    # print(f'Tempo de execução: {hora_impressao - hora_import}')

except ImportError as e:
    print ('Error ao obter dados: ', e)
