import nest_asyncio
nest_asyncio.apply()

import asyncio
from multiprocessing import Pool, cpu_count
import concurrent.futures
import time
from enum import Enum
import aiohttp
import requests
import certifi
import ssl

def get_ids_cervejarias():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    if r.status_code == 200:
        return [brewery['id'] for brewery in r.json()]

def get_cervejaria(id_c):
    url = f'https://api.openbrewerydb.org/breweries/{id_c}'
    r = requests.get(url)
    if r.status_code == 200:
        print(r.json())

async def get_cervejaria_async(id_c, session):
    async with session.get(f'https://api.openbrewerydb.org/breweries/{id_c}') as response:
        if response.status == 200:
            print(await response.json())

async def processar_async(ids):
    coros = []
    # Criar o contexto SSL usando o módulo ssl
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    connector = aiohttp.TCPConnector(ssl=ssl_context)  # Passar o contexto SSL para o conector
    async with aiohttp.ClientSession(connector=connector) as session:
        for id_c in ids:
            coros.append(get_cervejaria_async(id_c, session))
        await asyncio.gather(*coros)

async def get_cervejaria_async_manual(id_c):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, get_cervejaria, id_c)

class TipoExecucao(Enum):
    UM_PROCESSO = 1
    VARIAS_THREADS = 2
    ASYNCIO_COM_LIB_HTTP = 3

if __name__ == '__main__':
    started = time.time()
    tipo_exec = TipoExecucao.ASYNCIO_COM_LIB_HTTP
    cores = cpu_count()

    ids_cervejarias = get_ids_cervejarias()

    if TipoExecucao.UM_PROCESSO == tipo_exec:
        for id_cervejaria in ids_cervejarias:
            get_cervejaria(id_cervejaria)
    elif TipoExecucao.VARIAS_THREADS == tipo_exec:
        with concurrent.futures.ThreadPoolExecutor(cores) as thp:
            thp.map(get_cervejaria, ids_cervejarias)
    elif TipoExecucao.ASYNCIO_COM_LIB_HTTP == tipo_exec:
        event_loop = asyncio.get_event_loop()
        tasks = []

        event_loop.run_until_complete(processar_async(ids_cervejarias))
    elapsed = time.time()
    print(f'Tempo total: {elapsed - started} segundos')