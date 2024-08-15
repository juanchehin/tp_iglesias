import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 'YYYYMMDD'
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# 
columna = df_2017['X1']

# 
valor_minimo = columna.min()

# Print
print(f"El valor mínimo de la columna 'X1' para el año 2017 es: {valor_minimo}")
