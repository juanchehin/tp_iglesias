import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# 
columna = df['X1']

# 
valor_minimo = columna.min()

# Print
print(f"El valor mínimo de la columna 'X1' es: {valor_minimo}")
