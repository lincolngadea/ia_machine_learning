from rx import of

if __name__ == "__main__":
    """
    Ponto de entrada: cria um Observable a partir de uma sequência fixa de valores 
    e conecta um Observer definido inline para processar o fluxo de dados.
    """
    source = of("Alfa", "Bravo", "Charlie", "Delta", "Echo")

    source.subscribe(
        on_next=lambda x: print(f"Received: {x}"),
        on_completed=lambda: print("Completed"),
        on_error=lambda e: print(f"Error: {e}")
    )