from threading import Thread  # Importa a classe Thread para criar threads.
from time import sleep  # Importa a função sleep para simular o tempo de processamento.
from threading import Lock  # Importa a classe Lock para sincronizar o acesso ao recurso compartilhado.

# Classe que representa uma padaria com um estoque de pães.
class Padaria:
    def __init__(self, estoque):
        self.estoque = estoque  # Inicializa o estoque de pães.
        self.lock = Lock()  # Cria um Lock para sincronizar as threads que acessam o estoque.

    # Metodo para comprar pães.
    def comprar_pao(self, quantidade):
        self.lock.acquire()  # Adquire o Lock para garantir que apenas uma thread acesse o estoque por vez.
        if self.estoque < quantidade:  # Verifica se há estoque suficiente para a compra.
            print(f"Estoque insuficiente!!")  # Exibe uma mensagem de erro se o estoque for insuficiente.
            self.lock.release()  # Libera o Lock antes de retornar.
            return
        sleep(1)  # Simula o tempo necessário para processar a compra.
        self.estoque -= quantidade  # Reduz a quantidade comprada do estoque.
        if quantidade == 1:  # Verifica se foi comprado apenas um pão.
            print(f"Você comprou {quantidade} pão.\
              Ainda temos {self.estoque} no estoque")  # Exibe a mensagem para um pão.
        else:
            print(f"Você comprou {quantidade} pães.\
                  ainda temos {self.estoque} no estoque")  # Exibe a mensagem para múltiplos pães.
        self.lock.release()  # Libera o Lock para que outras threads possam acessar o estoque.

# Bloco principal do programa.
if __name__ == "__main__":
    padaria = Padaria(20)  # Cria uma instância da classe Padaria com 20 pães no estoque.
    for i in range(1, 20):  # Cria 19 threads, cada uma tentando comprar uma quantidade diferente de pães.
        t = Thread(target=padaria.comprar_pao, args=(i,))  # Define a função `comprar_pao` como alvo da thread.
        t.start()  # Inicia a execução da thread.