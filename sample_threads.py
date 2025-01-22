from time import sleep  # Importa a função sleep para pausar a execução do programa por um tempo especificado.

# Exemplo de um processo sequencial...
# for i in range(10):
#     sleep(.5)  # Pausa de 0.5 segundos para cada execução.
#     print(i)  # Imprime o valor atual de i.

# Apresentando um processo com thread
from threading import Thread  # Importa a classe Thread para criar e gerenciar threads.

# Define uma classe personalizada que herda de Thread.
class IGThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto  # Texto que será exibido quando a thread for executada.
        self.tempo = tempo  # Tempo de pausa antes de exibir o texto.
        super().__init__()  # Chama o construtor da classe base Thread.

    # Metodo que será executado quando a thread for iniciada.
    def run(self):
        sleep(self.tempo)  # Pausa a execução da thread pelo tempo especificado.
        print(self.texto)  # Imprime o texto associado à thread.

# Criação de instâncias da classe IGThread com diferentes textos e tempos de pausa.
t1 = IGThread('IGTI Thread 1', 5)  # Cria uma thread que espera 5 segundos antes de imprimir.
t1.start()  # Inicia a execução da thread.
t2 = IGThread('IGTI Thread 2', 8)  # Cria uma thread que espera 8 segundos antes de imprimir.
t2.start()  # Inicia a execução da thread.
t3 = IGThread('IGTI Thread 3', 17)  # Cria uma thread que espera 17 segundos antes de imprimir.
t3.start()  # Inicia a execução da thread.
t4 = IGThread('IGTI Thread 4', 2)  # Cria uma thread que espera 2 segundos antes de imprimir.
t4.start()  # Inicia a execução da thread.

# Loop principal que executa em paralelo às threads.
for i in range(20):  # Itera de 0 a 19.
    print(i)  # Imprime o valor atual de i.
    sleep(1)  # Pausa a execução do loop por 1 segundo.