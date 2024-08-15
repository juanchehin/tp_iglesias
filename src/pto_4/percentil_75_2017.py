import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# 2017
df_2017 = df[df['YYYYMMDD'].dt.year == 2017]

# 
columna = df_2017['X1']  # 'X1'

# percentil 75
percentil_75 = columna.quantile(0.75)

# Print
print(f"El percentil 75 de la columna 'X1' para el año 2017 es: {percentil_75}")
