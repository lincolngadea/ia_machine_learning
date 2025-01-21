import pandas as pd

# Lê o arquivo CSV e cria um DataFrame
df = pd.read_csv("census.csv")

# Exibe a quantidade de registros (linhas e colunas) no DataFrame
print(df.shape)

# Separa as variáveis independentes (colunas 0 a 13) e a variável dependente (coluna 14)
x = df.iloc[:, 0:14].values
y = df.iloc[:, 14].values

from sklearn.preprocessing import LabelEncoder

# Codificação de variáveis categóricas para valores numéricos
label_encoder = LabelEncoder()
x[:, 1] = label_encoder.fit_transform(x[:, 1])  # Codifica a coluna 1
x[:, 3] = label_encoder.fit_transform(x[:, 3])  # Codifica a coluna 3
x[:, 5] = label_encoder.fit_transform(x[:, 5])  # Codifica a coluna 5
x[:, 6] = label_encoder.fit_transform(x[:, 6])  # Codifica a coluna 6
x[:, 7] = label_encoder.fit_transform(x[:, 7])  # Codifica a coluna 7
x[:, 8] = label_encoder.fit_transform(x[:, 8])  # Codifica a coluna 8
x[:, 9] = label_encoder.fit_transform(x[:, 9])  # Codifica a coluna 9
x[:, 13] = label_encoder.fit_transform(x[:, 13])  # Codifica a coluna 13

from sklearn.preprocessing import StandardScaler

# Normalização dos dados para média 0 e desvio padrão 1
scaler_x = StandardScaler()
x = scaler_x.fit_transform(x)

from sklearn.model_selection import train_test_split

# Divide os dados em conjuntos de treinamento (80%) e teste (20%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Exibe o tamanho dos conjuntos de treinamento e teste
print("Treinamento de X:", x_train.shape)
print("Treinamento de Y:", y_train.shape)
print("########################")
print("Teste de X:", x_test.shape)
print("Teste de Y:", y_test.shape)

from sklearn.linear_model import LogisticRegression

# Cria e treina o modelo de Regressão Logística
classificador = LogisticRegression(max_iter=12000)  # Define o número máximo de iterações
classificador.fit(x_train, y_train)

# Faz previsões nos dados de teste
previsoes = classificador.predict(x_test)

# Exibe as previsões e os valores reais do conjunto de teste
print("Bases de treinamento dos dados:", previsoes)
print("Bases de Teste dos dados:", y_test)

from sklearn.metrics import accuracy_score

# Calcula e exibe a precisão do modelo
precisao = accuracy_score(y_test, previsoes)
print("Precisão:", precisao)