def soma(a, b):
    try:
        test_a = a + 1
        test_b = b + 1
    except TypeError:
        print(
            f"Os inputs A e B devem ser int ou float. Recebemos {a}: {type(a)}, e {b}: {type(b)}")
    else:
        return a + b


def subtracao(a, b):
    return a - b

