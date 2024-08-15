import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 
columnas = df[['Y','X1', 'X2']] 

# 
matriz_covarianza = columnas.cov()

# Print
print("Matriz de covarianza:")
print(matriz_covarianza)
