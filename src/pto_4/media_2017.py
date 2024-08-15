import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# 
columna = df_2017['X1']

# 
media = columna.mean()

# Print
print(f"La media de la columna 'X1' para el año 2017 es: {media}")
