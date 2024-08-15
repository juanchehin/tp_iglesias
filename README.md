# TP Iglesias

Use the provided CSV file to perform the following steps:
 
 
 
1. Calculate the mean, 75th percentile, min values
2. Regress Y on X1 and X2
3. Find the covariance matrix
 
4. Repeat steps 1-3 but only for data starting 2017 and later

Hint:
1) To calculate the covariance using Numpy, change the line: 
coefficients = np.polyfit(X, y, 1)
to:
coefficients, cov_matrix = np.polyfit(X, y, 1, cov=True)
2) For the mean, 75th percentile, and min values, and assuming that you have assigned the independent variable to X and the dependent variable to y, use the following methods on each X, y:
.mean()
.min()
.quantile(0.75)

## Traduccion español

Utilice el archivo CSV proporcionado para realizar los siguientes pasos:
1. Calcular la media, el percentil 75 y los valores mínimos.
2. Regrese Y en X1 y X2
3. Encuentra la matriz de covarianza
4. Repita los pasos 1 a 3, pero solo para los datos a partir de 2017.

Pista:
1) Para calcular la covarianza usando Numpy, cambie la línea:
coeficientes = np.polyfit(X, y, 1)
a:
coeficientes, cov_matrix = np.polyfit(X, y, 1, cov=True)
2) Para los valores medio, percentil 75 y mínimo, y suponiendo que ha asignado la variable independiente a X y la variable dependiente a y, utilice los siguientes métodos en cada X, y:
.significar()
.min()
.cuantil(0,75)