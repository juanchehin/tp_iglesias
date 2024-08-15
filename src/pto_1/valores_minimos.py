import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# Columna de interés
columna = df['X1']

# Calcular
valor_minimo = columna.min()

# Imprimir los resultados
print(f"El valor mínimo de la columna 'X1' es: {valor_minimo}")
