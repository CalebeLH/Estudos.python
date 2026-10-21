nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota:"))
nome = input("Digite o nome do aluno: ")

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

resultado = calcular_media(nota1, nota2, nota3)
print("Olá, ", nome, "a sua média é: ", resultado)

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"


for idx in range(1, 11, 2):
    print("Repetição número: ", idx)