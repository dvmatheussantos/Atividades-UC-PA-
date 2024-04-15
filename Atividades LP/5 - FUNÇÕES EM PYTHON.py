"""Atividade 1"""

def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ""
        for j in range(i):
            linha += str(i) + " "
        print(linha)

n = int(input("Digite um número inteiro: "))
imprimir_padrao(n)

"""Atividade 2"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número inteiro para calcular o fatorial: "))
print("O fatorial de", numero, "é:", fatorial(numero))

"""Atividade 3"""

def p(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

n = int(input("Digite um número inteiro para verificar se é primo: "))
if p(n):
    print(n, "é primo.")
else:
    print(n, "não é primo.")

"""Atividade 4"""

def invertes(s):
    return s[::-1]

t = input("Digite uma string para inverter: ")
print("String invertida:", invertes(t))

"""Atividade 5"""

def maior_valor(lista):
    if len(lista) == 0:
        return None

    maximo = lista[0]

    for num in lista:
        if num > maximo:
            maximo = num

    return maximo
numero = [3, 5, 9, 12, 34, 61, 4, 54]

print("O maior número é:", maior_valor(numero))

"""Atividade 6"""

def conta_vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']

    contador = 0

    for char in texto:
        char = char.lower()
        if char in vogais:
            contador += 1

    return contador

texto = "A mig"
print("Número de vogais:", conta_vogais(texto))

"""Atividade 7"""

def soma_quadrados(lista):
    if len(lista) == 0:
        return None

    soma = lista[0]

    for num in lista:
        soma += num ** 2

    return soma
numero = [3, 5, 9, 12, 34, 61, 4, 54]

print("A soma dos quandrado dos números é:", soma_quadrados(numero))

"""Atividade 8"""

def imprima_tabuada(numero):
  print(f"Tabuada do {numero}:")
  for i in range(1, 11):
      resultado = numero * 1
      print(f"{numero} x {i} = {resultado}")

imprima_tabuada(2)
