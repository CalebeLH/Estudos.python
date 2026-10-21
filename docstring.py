valor_a = float(input("Digite um valor:"))
valor_b = float(input("Digite um segundo:"))

def somar(valor_a, valor_b):
    """
    Realize a soma entre dois números.

    Args:
        valor_a (float): Primeiro valor
        valor_b (float): Segundo valor

    Return:
        float: Resultado da soma.
    """
    soma = valor_a + valor_b
    return soma

soma = somar(valor_a, valor_b)
print(soma)
