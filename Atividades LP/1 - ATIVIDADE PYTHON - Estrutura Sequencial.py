"""Atividade 1"""

print("Hello  world")

"""Atividade 2"""

numero= int(input("Escreva um numero inteiro:  "))

print (numero)

"""Atividade 3"""

A = float(input("Escreva um número: "))
B = float(input("Escreva um outro número: "))

print("A soma dos números é: ", A + B)

"""Atividade 4"""

A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota: "))
C = float(input("Digite a terceira nota: "))
D = float(input("Digite a quarta nota: "))

E = A + B + C + D

print("Sua média é: ", E / 4)

"""Atividade 5"""

A = float(input("Digite quantos metros você deseja converter para centímetros: "))

B = A * 100

print("A conversão em centímetros é: ", B)

"""Atividade 6"""

raio = float(input("Digite o raio do criculo: "))

area = 3.14 * raio ** 2

print("o área do criculo: ", area)

"""Atividade 7"""

A = float(input("Digite o primeiro lado do quadrado: "))

B = A * A

print("A aréa do quadrado é: ", B)


print("O dobro da aréa é: ", B * 2)

"""Atividade 8"""

A = float(input("Quanto você ganha por hora: "))
B= float(input("Quantas horas você trabalha no mês: "))

C = A * B

print("Atualmente você ganha", C, " No mês")

"""Atividade 9"""

F = float(input("Digite a temperatura em graus Fahrenheit: "))

c = 5 * ((F-32) / 9)

print("A temperatura em graus celsiues é: ", c)

"""Atividade 10"""

C = float(input("Digite a temperatura em graus celsiues: "))

F = (C * 9/5) + 32

print("A temperatura em fahrenheit é: ", F)

"""Atividade 11"""

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

resultado1 = (2 * num1) * (num2 / 2)
resultado2 = (3 * num1) + num_real
resultado3 = num_real ** 3

print("O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("A soma do triplo do primeiro com o terceiro é:", resultado2)
print("O terceiro elevado ao cubo é:", resultado3)

"""Atividade 12"""

peso = float(input("Digite o peso dos peixes em quilos: "))
excesso = max(0, peso - 50)
multa = excesso * 4

print("Excesso de peso:", excesso, "quilos")
print("Valor da multa a pagar: R$", multa)

"""Atividade 13"""

ganhoh = float(input("Digite quanto você ganha por hora: "))
horast = float(input("Digite o número de horas trabalhadas no mês: "))

salariob = ganhoh * horast

ir = salariob * 0.11
inss = salariob * 0.08
sindicato = salariob * 0.05

salariol = salariob - ir - inss - sindicato

print("Salário Bruto: R$",  salariob)
print("Desconto do INSS: R$", inss)
print("Desconto do Sindicato: R$", sindicato)
print("Salário Líquido: R$", salariol)

"""Atividade 14"""

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_tinta = area / 3
quantidade_latas = math.ceil(litros_tinta / 18)
preco_total = quantidade_latas * 80

print("Quantidade de latas de tinta a serem compradas:", quantidade_latas)
print("Preço total: R$", preco_total)

"""Atividade 15"""

import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_tinta = area / 6

quantidade_latas = math.ceil((litros_tinta * 1.1) / 18)

preco_latas = quantidade_latas * 80

quantidade_galoes = math.ceil((litros_tinta * 1.1) / 3.6)

preco_galoes = quantidade_galoes * 25

quantidade_latas_misturadas = math.floor(litros_tinta / 18)
resto = litros_tinta % 18
quantidade_galoes_misturados = math.ceil((resto * 1.1) / 3.6)

preco_mistura = (quantidade_latas_misturadas * 80) + (quantidade_galoes_misturados * 25)

print("Quantidade de latas de tinta a serem compradas:", quantidade_latas)
print("Preço total para comprar apenas latas: R$", preco_latas)
print("Quantidade de galões de tinta a serem comprados:", quantidade_galoes)
print("Preço total para comprar apenas galões: R$", preco_galoes)
print("Quantidade de latas de tinta na mistura:", quantidade_latas_misturadas)
print("Quantidade de galões de tinta na mistura:", quantidade_galoes_misturados)
print("Preço total para a mistura de latas e galões: R$", preco_mistura)

"""Atividade 16"""

tamanho_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

tamanho_mbps = tamanho_mb * 8

tempo = (tamanho_mbps / velocidade_mbps) / 60

print("Tempo aproximado de download:", round(tempo, 2), "minutos")
