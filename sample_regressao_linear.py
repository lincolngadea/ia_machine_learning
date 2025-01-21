import numpy as np
import matplotlib.pyplot as plt
import random

# Gerar matriz de 20 alturas fixas (em cm)
matriz_alturas = [
    [120], [110], [120], [150], [140], [177], [150], [160], [180], [190],
    [140], [195], [155], [160], [165], [175], [185], [195], [198], [199]
]

# Gerar matriz de 20 pesos fixos (em kg)
matriz_pesos = [
    [77], [67], [75], [75], [65], [78], [66], [70], [82], [91],
    [77], [102], [67], [77], [78], [77], [97], [110], [120], [112]
]

# Exibe um gráfico de dispersão (scatter plot) com as alturas no eixo X e os pesos no eixo Y
plt.scatter(matriz_alturas, matriz_pesos)
plt.xlabel('Altura (cm)')  # Rótulo do eixo X
plt.ylabel('Peso (kg)')    # Rótulo do eixo Y
# plt.show()  # Exibe o gráfico (descomentando esta linha)

# Importa o modelo de Regressão Linear da biblioteca sklearn
from sklearn.linear_model import LinearRegression

# Cria e treina o modelo de Regressão Linear com os dados de altura e peso
regressor = LinearRegression().fit(matriz_alturas, matriz_pesos)

# Obtém o intercepto (b0) e o coeficiente angular (b1) da reta ajustada
intercept = regressor.intercept_  # Intercepto da reta
coeficient = regressor.coef_      # Coeficiente angular (inclinação)

# Calcula as previsões usando a fórmula da regressão linear: y = b0 + b1 * x
previsoes = regressor.predict(matriz_alturas)

# Calcula a diferença entre os valores reais e as previsões
validador_previsoes = (matriz_pesos - previsoes)  # Diferença entre pesos reais e previstos
# print(validador_previsoes)

# Calcula o valor absoluto das diferenças
validador_abs_previsoes = abs(matriz_pesos - previsoes)  # Diferença absoluta
# print(validador_abs_previsoes)

# Calcula a média das diferenças absolutas
validador_med_previsoes = abs(matriz_pesos - previsoes).mean()  # Média das diferenças absolutas
# print(validador_med_previsoes)

# Importa métricas de erro da biblioteca sklearn
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Calcula o erro absoluto médio (MAE)
mae = mean_absolute_error(matriz_pesos, previsoes)  # Erro absoluto médio
# print(mae)

# Calcula o erro quadrático médio (MSE)
mse = mean_squared_error(matriz_pesos, previsoes)  # Erro quadrático médio
# print(mse)

# Exibe o gráfico com os dados reais e a reta ajustada pela regressão linear
plt.plot(matriz_alturas, matriz_pesos, 'o')  # Dados reais (pontos)
plt.plot(matriz_alturas, previsoes, color='red')  # Reta ajustada (em vermelho)
plt.title('Regressão Linear Simples')  # Título do gráfico
plt.xlabel('Altura (cm)')  # Rótulo do eixo X
plt.ylabel('Peso (kg)')    # Rótulo do eixo Y
# plt.show()  # Exibe o gráfico (descomentando esta linha)