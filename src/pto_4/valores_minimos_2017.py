import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# Convertir la columna 'YYYYMMDD' a formato de fecha
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# Filtrar los datos para el año 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# Columna de interés
columna = df_2017['X1']

# Calcular el valor mínimo
valor_minimo = columna.min()

# Imprimir el resultado
print(f"El valor mínimo de la columna 'X1' para el año 2017 es: {valor_minimo}")
