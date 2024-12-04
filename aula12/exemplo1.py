import pandas as pd
import polars as pl
from datetime import datetime
import gc # garbage collector

try:
    ENDEREÇO_DADOS = r'./dados/'

    # hora de inicio
    hora_import = datetime.now()

    df_janeiro = pl.read_csv(ENDEREÇO_DADOS + '202401_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')

    print(df_janeiro.head())

    hora_impressao = datetime.now()

    print(f'Tempo de execução: {hora_impressao - hora_import}')

except ImportError as e:
    print ('Error ao obter dados: ', e)
