from threading import Thread
from time import sleep
from threading import Lock

class Padaria:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # Criar um Lock para sincronizar as threads de compra de pães


    def comprar_pao(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print(f"Estoque insuficiente!!")
            self.lock.release()
            return
        sleep(1)
        self.estoque -= quantidade
        if quantidade == 1:
            print(f"Você comprou {quantidade} pão.\
              Ainda temos {self.estoque} no estoque")
        else:
            print(f"Você comprou {quantidade} pães.\
                  ainda temos {self.estoque} no estoque")
        self.lock.release()

if __name__ == "__main__":
    padaria = Padaria(20)
    for i in range(1,20):
        t = Thread(target=padaria.comprar_pao, args=(i,))
        t.start()