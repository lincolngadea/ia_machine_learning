import pandas as pd

from sample_regressao_linear import previsoes

df = pd.read_csv("risco_credito.csv")

x = df.iloc[:,0:4].values
y = df.iloc[:,4].values

# print(x)

# Transformação do df de x em dados numéricos
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
x[:,0] = labelencoder.fit_transform(x[:,0])
x[:,1] = labelencoder.fit_transform(x[:,1])
x[:,2] = labelencoder.fit_transform(x[:,2])
x[:,3] = labelencoder.fit_transform(x[:,3])

# print(x)
from sklearn.tree import DecisionTreeClassifier

# Criando o modelo de classificação
arvore_risco_credito = DecisionTreeClassifier(criterion ='entropy')
arvore_risco_credito.fit(x,y)

importancias_risco_credito = arvore_risco_credito.feature_importances_

# print(importancias_risco_credito)

# classes da arvore de risco
classes_risco = arvore_risco_credito.classes_
# print(classes_risco)

import matplotlib.pyplot as plt
from sklearn import tree

previsoes = ['historia','divida','garantias','renda']
figura, eixos = plt.subplots(nrows=1, ncols=1, figsize=(10,10))
tree.plot_tree(arvore_risco_credito, feature_names=previsoes, class_names=classes_risco, filled=True)
plt.show()
#previsão de riscos
previsoes = arvore_risco_credito.predict([[0,0,0,2]])
print(previsoes)
# print(df.columns)