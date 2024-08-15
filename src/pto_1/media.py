import pandas as pd

# DataFrame
df = pd.read_csv('D:/dev/tp_iglesias/HW-Javier.csv')

# Media Y, X1 y X2
media_Y = df['Y'].mean()
media_X1 = df['X1'].mean()
media_X2 = df['X2'].mean()

# Print
print(f"Media de la columna Y: {media_Y}")
print(f"Media de la columna X1: {media_X1}")
print(f"Media de la columna X2: {media_X2}")