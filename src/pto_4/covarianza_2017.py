import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# 
columnas = df_2017[['X1', 'X2']]

# 
matriz_covarianza = columnas.cov()

# Print
print("Matriz de covarianza:")
print(matriz_covarianza)
