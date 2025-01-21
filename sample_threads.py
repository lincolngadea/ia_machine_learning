from time import sleep

# Exemplo de um processo sequencial...
# for i in range(10):
#     sleep(.5)  # Pausa de 1 segundo para cada execução
#     print(i)

# Apresentando um processo com thread
from threading import Thread

class IGThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)  # Pausa de tempo segundo
        print(self.texto)

t1 = IGThread('IGTI Thread 1', 5)
t1.start()
t2 = IGThread('IGTI Thread 2', 8)
t2.start()
t3 = IGThread('IGTI Thread 3', 17)
t3.start()
t4 = IGThread('IGTI Thread 4', 2)
t4.start()



for i in range(20):
    print(i)
    sleep(1)  # Pausa de 0.5 segundo para cada execução
