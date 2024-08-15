import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# Convertir la columna 'YYYYMMDD' a formato de fecha
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# Filtrar los datos para el año 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# Columnas de interés
columnas = df_2017[['X1', 'X2']]

# Calcular la matriz de covarianza
matriz_covarianza = columnas.cov()

# Imprimir la matriz de covarianza
print("Matriz de covarianza:")
print(matriz_covarianza)
