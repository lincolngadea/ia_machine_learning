import nest_asyncio
nest_asyncio.apply()  # Permite que o loop de eventos do asyncio seja reutilizado em ambientes que não permitem isso, como notebooks Jupyter.

import asyncio
from multiprocessing import Pool, cpu_count  # Para trabalhar com múltiplos processos.
import concurrent.futures  # Para trabalhar com múltiplas threads.
import time
from enum import Enum  # Para criar um enumerador que define os tipos de execução.
import aiohttp  # Biblioteca para requisições HTTP assíncronas.
import requests  # Biblioteca para requisições HTTP síncronas.
import certifi  # Fornece um conjunto de certificados confiáveis.
import ssl  # Para criar um contexto SSL seguro.

# Função para obter os IDs das cervejarias usando uma requisição síncrona.
def get_ids_cervejarias():
    r = requests.get('https://api.openbrewerydb.org/breweries')  # Faz uma requisição para obter a lista de cervejarias.
    if r.status_code == 200:  # Verifica se a requisição foi bem-sucedida.
        return [brewery['id'] for brewery in r.json()]  # Retorna uma lista com os IDs das cervejarias.

# Função síncrona para obter os detalhes de uma cervejaria pelo ID.
def get_cervejaria(id_c):
    url = f'https://api.openbrewerydb.org/breweries/{id_c}'  # Monta a URL com o ID da cervejaria.
    r = requests.get(url)  # Faz a requisição HTTP.
    if r.status_code == 200:  # Verifica se a requisição foi bem-sucedida.
        print(r.json())  # Imprime os detalhes da cervejaria.

# Função assíncrona para obter os detalhes de uma cervejaria pelo ID.
async def get_cervejaria_async(id_c, session):
    async with session.get(f'https://api.openbrewerydb.org/breweries/{id_c}') as response:  # Faz a requisição HTTP assíncrona.
        if response.status == 200:  # Verifica se a requisição foi bem-sucedida.
            print(await response.json())  # Imprime os detalhes da cervejaria.

# Função para processar os IDs das cervejarias de forma assíncrona.
async def processar_async(ids):
    coros = []  # Lista para armazenar as corrotinas.
    # Criar o contexto SSL usando o módulo ssl
    ssl_context = ssl.create_default_context(cafile=certifi.where())  # Cria um contexto SSL seguro.
    connector = aiohttp.TCPConnector(ssl=ssl_context)  # Passa o contexto SSL para o conector.
    async with aiohttp.ClientSession(connector=connector) as session:  # Cria uma sessão HTTP assíncrona.
        for id_c in ids:  # Para cada ID de cervejaria...
            coros.append(get_cervejaria_async(id_c, session))  # Adiciona a corrotina para obter os detalhes da cervejaria.
        await asyncio.gather(*coros)  # Executa todas as corrotinas de forma concorrente.

# Função para executar uma tarefa síncrona em um executor assíncrono.
async def get_cervejaria_async_manual(id_c):
    loop = asyncio.get_running_loop()  # Obtém o loop de eventos atual.
    return await loop.run_in_executor(None, get_cervejaria, id_c)  # Executa a função síncrona em um executor.

# Enum para definir os tipos de execução disponíveis.
class TipoExecucao(Enum):
    UM_PROCESSO = 1  # Execução síncrona em um único processo.
    VARIAS_THREADS = 2  # Execução usando múltiplas threads.
    ASYNCIO_COM_LIB_HTTP = 3  # Execução assíncrona usando a biblioteca aiohttp.

if __name__ == '__main__':
    started = time.time()  # Marca o tempo de início.
    tipo_exec = TipoExecucao.ASYNCIO_COM_LIB_HTTP  # Define o tipo de execução desejado.
    cores = cpu_count()  # Obtém o número de núcleos da CPU.

    ids_cervejarias = get_ids_cervejarias()  # Obtém os IDs das cervejarias.

    # Executa o código de acordo com o tipo de execução escolhido.
    if TipoExecucao.UM_PROCESSO == tipo_exec:
        for id_cervejaria in ids_cervejarias:  # Para cada ID de cervejaria...
            get_cervejaria(id_cervejaria)  # Obtém os detalhes da cervejaria de forma síncrona.
    elif TipoExecucao.VARIAS_THREADS == tipo_exec:
        with concurrent.futures.ThreadPoolExecutor(cores) as thp:  # Cria um pool de threads.
            thp.map(get_cervejaria, ids_cervejarias)  # Executa a função em múltiplas threads.
    elif TipoExecucao.ASYNCIO_COM_LIB_HTTP == tipo_exec:
        event_loop = asyncio.get_event_loop()  # Obtém o loop de eventos.
        tasks = []

        event_loop.run_until_complete(processar_async(ids_cervejarias))  # Executa a função assíncrona.
    elapsed = time.time()  # Marca o tempo de término.
    print(f'Tempo total: {elapsed - started} segundos')  # Imprime o tempo total de execução.