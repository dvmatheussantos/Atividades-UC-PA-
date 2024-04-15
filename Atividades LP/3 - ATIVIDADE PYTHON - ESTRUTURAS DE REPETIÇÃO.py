
"""Ativiade 1"""

while True:

  nota = float(input("Digite uma nota entre zero e dez: "))

  print("")

  if 0 <= nota <= 10:
    print("Nota válida:", nota)
    break

  else:
      print("Nota inválida. Por favor, digite uma nota entre zero e dez.")

"""Ativiade 2"""

while True:
    nome = input("Digite seu nome de usuario: ")
    senha = input("Digite sua senha: ")

    if senha != nome:
        print("Usuario e senha salvos com sucesso.")
        break

    else:
        print("Erro: Sua senha não pode ser igua seu nome. Por favor, tente novamente")

"""Ativiade 3"""

for i in range (1,21):
  print(i)

for i in range (1,21):
  print(i, end="")

"""Atividade 4"""

numeros = input("Informe 5 números separados por espaços: ")

numeros_separados = numeros.split()

n1, n2, n3, n4, n5 = map(float, numeros_separados)

maior = max(n1, n2, n3, n4, n5)

print(f"O maior número é {maior}")

"""Ativiade 5"""

soma = 0
quantidade_numeros = 5

for i in range(quantidade_numeros):
    numero = float(input("Digite um número: "))
    soma += numero

media = soma / quantidade_numeros

print("Soma dos números:", soma)
print("Média dos números:", media)

"""Atividade 6"""

for numero in range(1, 51):
    if numero % 2 != 0:
        print(numero)

"""Atividade 7"""

n1 = float(input("Digite um númeor: "))
n2 = float(input("Digite um segund número: "))

n1_int = int(n1)
n2_int = int(n2)

for i in range(n1_int, n2_int + 1):
        print(i)

"""Atividade 8"""

n = int(input("Digite um número para ver a tabuada (1 a 10): "))

print("Tabuada de", n, ":")
for i in range(1, 11):
    resultado = n * i
    print(n, "X", i, "=", resultado)

"""Atividade 9"""

b = int(input("Digite a base: "))
expo = int(input("Digite o expoente: "))

r = 1

for i in range(expo):
    r *= b

print("Resultado:", r)

"""Ativiade 10"""

pares = 0
impares = 0

for _ in range(10):
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

"""Atividade 11"""

n = int(input("Digite o valor de n para a série de Fibonacci: "))

termo_anterior = 1
termo_atual = 1

print("Série de Fibonacci até o", n, "º termo:")
print(termo_anterior)
print(termo_atual)

for _ in range(2, n):
    proximo_termo = termo_anterior + termo_atual
    print(proximo_termo)
    termo_anterior = termo_atual
    termo_atual = proximo_termo

"""Atividade 12"""

limite = 500
a, b = 0, 1
print("Série de Fibonacci até que o valor seja maior que", limite, ":")
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b

"""Atividade 13"""

n = int(input("Digite um número para calcular o fatorial: "))
f = 1

for i in range(1, n + 1):
    f *= i

print("O fatorial de", n, "é:", f)
