import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 
columna = df['X1']

# 
percentil_75 = columna.quantile(0.75)

# Print
print(f"El percentil 75 de la columna 'X1' es: {percentil_75}")
