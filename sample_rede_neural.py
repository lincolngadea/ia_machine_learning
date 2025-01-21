import pandas as pd
from sample_regressao_logistica import previsoes

# Carrega o dataset de crédito
df = pd.read_csv("credit_data.csv")

# Remove valores nulos do dataset
df = df.dropna()

# Exibe o número de linhas e colunas do dataset após a limpeza
print(df.shape)

# Define as variáveis independentes (features) e dependente (target)
x_credit = df[['income', 'age', 'loan']]  # Features: renda, idade e empréstimo
y_credit = df[['default']]  # Target: se houve inadimplência (default)

from sklearn.preprocessing import StandardScaler

# Normaliza os dados para que todas as features tenham a mesma escala
standard_scaler = StandardScaler()
x_credit = standard_scaler.fit_transform(x_credit)

from sklearn.model_selection import train_test_split

# Divide os dados em conjuntos de treinamento e teste
# 75% para treinamento e 25% para teste
x_train, x_test, y_train, y_test = train_test_split(x_credit, y_credit, test_size=0.25, random_state=0)

# Exibe as dimensões dos conjuntos de treinamento e teste
print("Dados de treinamento X_credit:", x_train.shape)
print("Dados de treinamento Y_credit:", y_train.shape)
print("###################")
print("Dados de teste X_credit:", x_test.shape)
print("Dados de teste Y_credit:", y_test.shape)

from sklearn.neural_network import MLPClassifier

# Cria e configura uma rede neural com 2 camadas ocultas (20 e 100 neurônios)
# max_iter: número máximo de iterações
# tol: tolerância para o critério de parada
# verbose: exibe informações durante o treinamento
rede_neural_credit = MLPClassifier(max_iter=1000, verbose=True, tol=0.0000100, hidden_layer_sizes=(20, 100))

# Treina a rede neural com os dados de treinamento
rede_neural_credit.fit(x_train, y_train)

# Realiza previsões com os dados de teste
previsoes = rede_neural_credit.predict(x_test)

from sklearn.metrics import accuracy_score

# Calcula a taxa de acerto (acurácia) das previsões
taxa_acerto = accuracy_score(y_test, previsoes)
print("Taxa de acerto:", taxa_acerto)