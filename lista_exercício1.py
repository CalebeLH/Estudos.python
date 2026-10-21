#Lista de exercícios 1 - Python
#Aluno: Calebe Benedito Martins


#1)
ano = int(input("Digite o ano de nascimento: "))

idade = 2026 - ano
print("Sua idade atual é:", idade)



#2
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Não é possível dividir por zero."

operacao = input("Digite a operação desejada (soma, subtracao, multiplicacao, divisao): ")
if operacao == "soma":
    print("Resultado:", soma(n1, n2))
elif operacao == "subtracao":
    print("Resultado:", subtracao(n1, n2))
elif operacao == "multiplicacao":
    print("Resultado:", multiplicacao(n1, n2))
elif operacao == "divisao":
    print("Resultado:", divisao(n1, n2))


#3)
numero = float(input("Digite um número:"))

if numero%2 == 0:
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.")



#4)
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

if calcular_media(nota1, nota2, nota3) >= 7:
    print("Você foi aprovado com média:", calcular_media(nota1, nota2, nota3))
elif calcular_media(nota1, nota2, nota3) >= 5:
    print("Você está de recuperação com média:", calcular_media(nota1, nota2, nota3))
else:
    print("Você foi reprovado com média:", calcular_media(nota1, nota2, nota3))



#5)
numero = int(input("Digite um número inteiro:"))

print("A tabuada do número", numero, "é:")
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)



#6)
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (temperatura_celsius * 9 / 5) + 32
print("A temperatura em Farenheit é:", fahrenheit)


#7)
valor = float(input("Digite um valo em rais: "))
taxa = float(input("Digite a taxa de juros em porcentagem: "))
tempo = float(input("Digite o tempo em  anos: "))

juros = (valor * taxa * tempo) / 100
montante = valor + juros
print("O valor final com juros simples é:  R$", montante,)



#8)
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

print("O seu IMC é: ", imc)


