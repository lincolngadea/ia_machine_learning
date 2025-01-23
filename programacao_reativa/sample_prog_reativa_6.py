from rx import of, operators as op

of("Alpha", "Beta", "Gamma", "Delta", "Epslon").pipe(
    op.map(lambda x: x.upper()),  # Converte os caracteres para maiúsculo.
    op.filter(lambda x: len(x) > 4)  # Filtra os elementos com mais de 4 caracteres.
).subscribe(
    lambda value: print("Recebido {0}".format(value))
)