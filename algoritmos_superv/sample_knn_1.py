# Importações organizadas
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Carrega o dataset Iris
iris = datasets.load_iris()

# Converte os dados de entrada (características) e saída (classe) em DataFrame
df_iris = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])
print("Primeiras linhas do dataset:")
print(df_iris.head())

# Divide os dados em características (X) e rótulos (y)
X = df_iris.iloc[:, :-1].values
y = df_iris.iloc[:, -1].values

# Divide os dados em conjuntos de treinamento e teste (com random_state para reprodutibilidade)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normaliza os dados (aplica fit_transform no conjunto de treinamento e transform no conjunto de teste)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Treina o modelo KNN com 5 vizinhos
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# Realiza a previsão dos resultados
y_pred = classifier.predict(X_test)

# Cria a matriz de confusão e o relatório de classificação
cm = confusion_matrix(y_test, y_pred)
cr = classification_report(y_test, y_pred)
print("\nMatriz de Confusão:")
print(cm)
print("\nRelatório de Classificação:")
print(cr)

# Calcula e exibe a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAcurácia do modelo: {accuracy:.2f}")