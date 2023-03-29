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
    try:
        test_a = a + 1
        test_b = b + 1
    except TypeError:
        print(
            f"Os inputs A e B devem ser int ou float. Recebemos {a}: {type(a)}, e {b}: {type(b)}")
    else:
        return a - b


def divisao(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        div = 'infinito'
        print(f'1/{b} = {div}')
    except TypeError:
        div = f'1/{b}'
        print(f'1/{b} = {div}')
    except:
        div = 'erro desconhecido'
        print(f'1/{b} = {div}')
