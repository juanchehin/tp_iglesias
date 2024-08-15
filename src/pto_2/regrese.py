
import statsmodels.api as sm

#

X = df[ [ 'X1', 'x2']] 
y = df['Y']

# 
X = sm.add_constant (X)

# 
modelo =  sm.OLS (y, X).fit()

# Print
print (modelo.summary())