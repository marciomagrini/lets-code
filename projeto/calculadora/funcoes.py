def soma(a, b):
    try:
        return a + b
    except TypeError:
        print(
            f"Os inputs A e B devem ser int ou float. Recebemos {a}: {type(a)}, e {b}: {type(b)}")


def subtracao(a, b):
    return a - b
