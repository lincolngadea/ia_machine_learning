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
    Ao final, sinaliza a conclusão do processo.
    """
    for stock in stocks:
        if stock['PRICE'] > 100:
            observer.on_next(stock['TCKR'])
    observer.on_completed()

if __name__ == "__main__":
    """
    Ponto de entrada: cria o Observable baseado no filtro de ações
    e utiliza um Observer inline para processar os eventos.
    """
    source = create(buy_stock_events)
    source.subscribe(
        on_next=lambda x: print(f"Instruções recebidas para comprar ações {x}"),
        on_completed=lambda: print("Todos os ativos foram analisados. Não há mais ações para comprar."),
        on_error=lambda e: print(f"Erro durante a análise dos ativos: {e}")
    )