import numpy as np
import matplotlib.pyplot as plt
import random

# Gerar matriz de 100 alturas aleatórias entre 80 e 200
matriz_alturas = [
    [120], [110], [120], [150], [140], [177], [150], [160], [180], [190],
    [140], [195], [155], [160], [165], [175], [185], [195], [198], [199]
]

# Gerar matriz de 100 pesos aleatórios entre 70 e 120
matriz_pesos = [
    [77], [67], [75], [75], [65], [78], [66], [70], [82], [91],
    [77], [102], [67], [77], [78], [77], [97], [110], [120], [112]
]

# print(matriz_alturas)

# Exibe o gráfico
plt.scatter(matriz_alturas, matriz_pesos)
plt.xlabel('Peso (kg)')
plt.ylabel('Altura (cm)')
# plt.show()

# Calculando a previsão da regressação linear com sklearn
from sklearn.linear_model import LinearRegression

regressor = LinearRegression().fit(matriz_alturas, matriz_pesos)

# Verificando o intercept e o coeficiente dos dados
intercept = regressor.intercept_
coeficient = regressor.coef_

# Calculando a fórmula preditiva
previsoes = intercept + coeficient * matriz_alturas


previsoes = regressor.predict(matriz_alturas)
# print(previsoes)

validador_previsoes = (matriz_pesos - previsoes)
# print(validador_previsoes)

validador_abs_previsoes = abs(matriz_pesos - previsoes)
# print(validador_abs_previsoes)

validador_med_previsoes = abs(matriz_pesos - previsoes).mean()
# print(validador_med_previsoes)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(matriz_pesos, previsoes)
# print(mae)

mse = mean_squared_error(matriz_pesos, previsoes) #quadrado do erro
# print(mse)

# Plotando o gráfico antes do treinamento
plt.plot(matriz_alturas,matriz_pesos, 'o')
plt.plot(matriz_alturas, previsoes, color='red')
plt.title('Regressão Linear Simples')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
# plt.show()