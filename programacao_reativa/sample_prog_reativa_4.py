from rx import disposable, create

# Lista de ações com símbolos (TCKR) e preços
stocks = [
    {'TCKR': 'APPL', 'PRICE': 200},
    {'TCKR': 'GOOG', 'PRICE': 77},
    {'TCKR': 'AMZN', 'PRICE': 250},
    {'TCKR': 'AAPL', 'PRICE': 40},
    {'TCKR': 'GOOG', 'PRICE': 170},
    {'TCKR': 'AMZN', 'PRICE': 230}
]

# Define o comportamento do Observable: emite o símbolo das ações com preço acima de 100
def buy_stock_events(observer, scheduler):
    """
    Filtra as ações com preço acima de 100 e emite o símbolo (TCKR) para o Observer.
    """
    for stock in stocks:
        if stock['PRICE'] > 100:
            observer.on_next(stock['TCKR'])
    observer.on_completed()

# Implementa um Observer personalizado para processar os eventos relacionados às ações
class StockObserver(disposable.Disposable):
    """
    Observer que processa:
    - `on_next`: Recebe os símbolos de ações que atendem ao critério.
    - `on_completed`: Sinaliza o término do processo de análise.
    - `on_error`: Gerencia erros durante o processo.
    """
    def on_next(self, value):
        print(f"Instruções recebidas para comprar ações {value}")

    def on_completed(self):
        print("Todos os ativos foram analisados. Não há mais ações para comprar.")

    def on_error(self, error):
        print(f"Erro durante a análise dos ativos: {error}")

if __name__ == "__main__":
    """
    Ponto de entrada: cria o Observable baseado no filtro de ações e conecta
    um StockObserver para processar os eventos.
    """
    source = create(buy_stock_events)
    source.subscribe(StockObserver())