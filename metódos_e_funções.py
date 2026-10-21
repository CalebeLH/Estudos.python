n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))


def soma():
    soma = n1 + n2
    return soma

def subtracao():
    subtracao = n1 - n2
    return subtracao

def multiplicacao():
    multiplicacao = n1 * n2
    return multiplicacao

def divisao():
    divisao = n1 / n2
    return divisao

def imprimir(valor):
    print(valor)

imprimir(divisao())
imprimir(multiplicacao())
imprimir(subtracao())
imprimir(soma())
