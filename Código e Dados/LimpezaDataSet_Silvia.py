import pandas as pd

dataset = pd.read_csv('enade2012.csv', sep=';')
dataset

dataset.isnull() #verifica sem existem valores faltantes
dataset.isnull().sum() #soma os registros faltantes por atributos
dataset.dropna(inplace=True) #remove todas as linhas onde existe pelo menos um registro faltante
