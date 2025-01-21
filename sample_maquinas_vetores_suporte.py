from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import pandas as pd

dataset = pd.read_csv("Social_Network_Ads.csv")
# print(dataset.head())

X = dataset[['Age','EstimatedSalary']]
y = dataset[['Purchased']]

# Normalização dos dados
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Criando o modelo de SVM
svm = SVC(kernel='rbf', random_state=1, C=1.0)

# Treinando o modelo
svm.fit(X_train, y_train)

# Verificando a acurácia
y_pred = svm.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Exibindo a acurácia do modelo de SVM para os dados de teste
print(f'Acurácia: {accuracy}')