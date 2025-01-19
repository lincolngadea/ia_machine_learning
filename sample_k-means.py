import numpy as np
import random
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

idades_x = [random.randint(18,65) for _ in range(100)]
salarios_y = [random.randint(1800,5000) for _ in range(100)]

grafico = px.scatter(x=idades_x, y=salarios_y)
#grafico.show()
#
base_salario = np.array([[idade, salario] for idade, salario in zip(idades_x, salarios_y)])
#print(base_salario)

scaler_salario = StandardScaler()
base_salario = scaler_salario.fit_transform(base_salario)
#print(base_salario)

kmeans_salario = KMeans(n_clusters=3)
num_centroides = kmeans_salario.fit(base_salario)
# print(num_centroides)

#Calcula os centroides
centroides_salario = kmeans_salario.cluster_centers_
# print(centroides_salario)

#Apresenta a escala inversa dos dados treinados
scaler_salario.inverse_transform(kmeans_salario.cluster_centers_)

# Define a classificação do agrupamento dos dados por meio de rotulos
rotulos_salario = kmeans_salario.labels_
print(rotulos_salario)

# Apresenta o gráfico do resultado
grafico1 = px.scatter(x=base_salario[:,0], y=base_salario[:,1], color=rotulos_salario)
grafico2 = px.scatter(x=centroides_salario[:,0], y=centroides_salario[:,1], color=['red', 'green', 'blue'], size=[8,8,8])
grafico3 = go.Figure(data=grafico1.data + grafico2.data)
grafico3.show()