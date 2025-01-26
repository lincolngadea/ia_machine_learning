# Importação das bibliotecas necessárias
from pandas import DataFrame  # Manipulação de dados em formato tabular
import matplotlib.pyplot as plt  # Visualização de dados
from sklearn.cluster import KMeans  # Algoritmo K-Means

def validar_dados(dados):
    """
    Valida os dados de entrada para garantir que sejam numéricos.
    """
    if not all(isinstance(i, (int, float)) for i in dados['x'] + dados['y']):
        raise ValueError("Os dados devem conter apenas números.")

def executar_kmeans(dados, n_clusters=2, random_state=42):
    """
    Executa o algoritmo K-Means nos dados fornecidos.

    Args:
        dados (dict): Dicionário com as listas 'x' e 'y'.
        n_clusters (int): Número de clusters desejados.
        random_state (int): Semente aleatória para reprodutibilidade.

    Returns:
        tuple: DataFrame com os dados, labels dos clusters e coordenadas dos centroides.
    """
    # Validação dos dados
    validar_dados(dados)

    # Criação do DataFrame
    df = DataFrame(dados, columns=['x', 'y'])

    # Configuração e treinamento do modelo K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    kmeans.fit(df)

    # Retorna o DataFrame, os rótulos dos clusters e os centroides
    return df, kmeans.labels_, kmeans.cluster_centers_

def plotar_clusters(df, labels, centroides):
    """
    Plota os clusters e seus centroides.

    Args:
        df (DataFrame): DataFrame com os dados originais.
        labels (array): Rótulos dos clusters para cada ponto.
        centroides (array): Coordenadas dos centroides dos clusters.
    """
    # Plota os pontos de dados coloridos pelos clusters
    plt.scatter(df['x'], df['y'], c=labels.astype(float), s=50, alpha=0.5, label='Pontos de Dados')

    # Plota os centroides em vermelho
    plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=100, marker='X', label='Centroides')

    # Configuração do gráfico
    plt.xlabel("Número de Visitas ao Site")
    plt.ylabel("Número de Compras Realizadas")
    plt.title("Agrupamento K-Means")
    plt.legend()
    plt.grid(True)
    plt.show()

# Dados de entrada
dados = {
    'x': [25, 34, 22, 27, 33, 33, 31, 22, 35, 34, 67, 54, 57, 43, 50, 57, 59, 52,
          65, 47, 49, 48, 35, 33, 44, 45, 38, 43, 51, 46],
    'y': [79, 51, 53, 78, 59, 74, 73, 57, 69, 75, 51, 32, 40, 47, 53, 36, 35, 58,
          59, 50, 25, 28, 14, 12, 20, 5, 29, 27, 8, 7]
}

# Execução do K-Means
df, labels, centroides = executar_kmeans(dados)

# Visualização dos clusters
plotar_clusters(df, labels, centroides)