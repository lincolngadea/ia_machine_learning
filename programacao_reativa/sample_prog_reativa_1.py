import rx
import rx.operators as ops

# Criação de uma fonte de dados reativa a partir de uma lista de valores.
# A lista contém números e uma string para demonstrar como o fluxo lida com erros.
source = rx.from_iterable([1, 2, 3, 'abcde', 4, 5])

# Aplicação de operadores reativos no fluxo de dados.
# O operador `map` transforma cada elemento do fluxo, subtraindo 1.
# O operador `filter` filtra os elementos que são pares.
disposable = source.pipe(
    ops.map(lambda i: i - 1),  # Transforma os elementos do fluxo.
    ops.filter(lambda i: i % 2 == 0)  # Filtra apenas os elementos pares.
).subscribe(
    # Define o comportamento para cada evento do fluxo.
    on_next=lambda i: print("on_next: {}".format(i)),  # Executado para cada elemento processado.
    on_completed=lambda: print("on_completed"),  # Executado quando o fluxo é concluído.
    on_error=lambda e: print("on_error: {}".format(e))  # Executado quando ocorre um erro.
)

# Libera os recursos associados à assinatura do fluxo.
disposable.dispose()

# Indica que o programa foi finalizado.
print("Finalizado")