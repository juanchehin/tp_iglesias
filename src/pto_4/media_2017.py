import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# Convertir la columna 'YYYYMMDD' a formato de fecha
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# Filtrar los datos para el año 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# Columna de interés
columna = df_2017['X1']

# Calcular la media
media = columna.mean()

# Imprimir el resultado
print(f"La media de la columna 'X1' para el año 2017 es: {media}")
