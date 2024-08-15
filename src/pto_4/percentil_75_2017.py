import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# Convertir la columna 'YYYYMMDD' a formato de fecha
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# Filtrar los datos para el año 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# Seleccionar la columna de interés
columna = df_2017['X1']  # Reemplaza 'X1' con el nombre de tu columna

# Calcular el percentil 75
percentil_75 = columna.quantile(0.75)

# Imprimir el resultado
print(f"El percentil 75 de la columna 'X1' para el año 2017 es: {percentil_75}")
