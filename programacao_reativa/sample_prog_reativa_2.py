from rx import create, disposable

# Define o comportamento do Observable ao emitir valores para o Observer
def push_five_strings(observer, scheduler):
    """
    Emite uma sequência fixa de strings e conclui o fluxo.
    """
    for value in ["Hello", "World", "from", "ReactiveX", "Python"]:
        observer.on_next(value)
    observer.on_completed()

# Implementação personalizada de um Observer para manipulação de eventos do fluxo
class PrintObserver(disposable.Disposable):
    """
    Observer que processa eventos recebidos do Observable.
    - on_next: Lida com cada valor emitido.
    - on_completed: Executado ao final do fluxo.
    - on_error: Gerencia erros emitidos.
    """
    def on_next(self, value):
        print(f"Received {value}")

    def on_completed(self):
        print("Completed")

    def on_error(self, error):
        print(f"Error: {error}")

# Configura e conecta o Observer ao Observable
if __name__ == "__main__":
    """
    Ponto de entrada: cria o Observable com base na função 'push_five_strings' 
    e conecta um PrintObserver para processar o fluxo de dados.
    """
    source = create(push_five_strings)
    source.subscribe(PrintObserver())