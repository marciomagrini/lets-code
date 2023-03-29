from funcoes import soma
from funcoes import subtracao
from funcoes import divisao
from funcoes import multiplicacao


def calcule():
    num_a = float(input("Por favor, digite um primeiro número: \n"))
    num_b = float(input("Por favor, digite o segundo número: "))

    operations_list = ['soma', 'subtracao', 'divisao',
                       'multiplicacao', '+', '-', '/', '*']
    operation = 0

    while operation not in operations_list:
        operation = input(
            "Agora digite a operação matemática a ser realizada com esse número: ")

    if operation == "soma" OR operation == "+":
        result = soma(num_a, num_b)

    print(f"O resultado da operação foi: {result}")
