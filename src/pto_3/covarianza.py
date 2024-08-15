import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 
columnas = df[['Y','X1', 'X2']] 

# Calcular la matriz de covarianza
matriz_covarianza = columnas.cov()

# Imprimir la matriz de covarianza
print("Matriz de covarianza:")
print(matriz_covarianza)
