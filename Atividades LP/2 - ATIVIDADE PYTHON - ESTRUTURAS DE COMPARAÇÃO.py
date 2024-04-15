"""Atividade 1"""

valor = int(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")

"""Atividade 2"""

letra = input("Digite uma letra (F ou M): ")

if letra == 'F':
    print("F - Feminino")
elif letra == 'M':
    print("M - Masculino")
else:
    print("Sexo Inválido.")

"""Atividade 3"""

letra = input("Digite uma letra: ")

if letra.lower() in 'aeiou':
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

"""Atividade 4"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

"""Atividade 5"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
print("O maior número é:", maior)

"""Atividade 6"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print("O maior número é:", maior)
print("O menor número é:", menor)

"""Atividade 7"""

preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

menor_preco = min(preco1, preco2, preco3)

if menor_preco == preco1:
    print("Você deve comprar o primeiro produto.")
elif menor_preco == preco2:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")

"""Atividade 8"""

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

print("Números em ordem decrescente:", numeros)

"""Atividade 9"""

salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

print("Salário antes do reajuste:", salario)
print("Percentual de aumento aplicado:", percentual_aumento, "%")
print("Valor do aumento:", aumento)
print("Novo salário após o aumento:", novo_salario)

"""Atividade 10"""

lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Os lados formam um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os lados formam um triângulo isósceles.")
    else:
        print("Os lados formam um triângulo escaleno.")
else:
    print("Os lados não formam um triângulo.")
