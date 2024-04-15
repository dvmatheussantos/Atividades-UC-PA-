"""Atividade 1"""

idades = []
alturas = []

for i in range(5):
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i+1)))
    altura = float(input("Digite a altura da {}ª pessoa (em metros): ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

print("\nIdades e alturas na ordem inversa:")
for i in range(4, -1, -1):
    print("Idade: {} anos, Altura: {:.2f} metros".format(idades[i], alturas[i]))

"""Atividade 2"""

def soma_quadrados(vetor):
    soma = 0
    for numero in vetor:
        soma += numero ** 2
    return soma

vetor_a = []

print("Digite 10 numeros inteiros:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor_a.append(numero)

resultado = soma_quadrados(vetor_a)

print (f"A soma dos quadrados dos elementros do vetor é: {resultado}")

"""Atividade 3"""

vetor1 = []
vetor2 = []

print("Digite os elementos do primeiro vetor:")
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    vetor1.append(elemento)

print("\nDigite os elementos do segund2o vetor:")
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    vetor2.append(elemento)

vetor_intercalado = []

for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])

print("\nTerceiro vetor intercalado:")
print(vetor_intercalado)

"""Atividade 4"""

vetor1 = []
vetor2 = []
vetor3 = []

print("Digite os elementos do primeiro vetor:")
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    vetor1.append(elemento)

print("\nDigite os elementos do segundo vetor:")
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    vetor2.append(elemento)

print("\nDigite os elementos do terceiro vetor:")
for i in range(10):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    vetor3.append(elemento)

vetor_intercalado = []

for i in range(10):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])
    vetor_intercalado.append(vetor3[i])

print("\nQuarto vetor intercalado:")
print(vetor_intercalado)

"""Atividade 5"""

idades = []
alturas = []

for i in range(10):
    idade = int(input("Digite a idade do aluno {}: ".format(i + 1)))
    altura = float(input("Digite a altura do aluno {}: ".format(i + 1)))
    idades.append(idade)
    alturas.append(altura)

total_alturas = 0
contador = 0
for i in range(10):
    if idades[i] > 13:1
        total_alturas += alturas[i]
        contador += 1

if contador > 0:
    media_alturas = total_alturas / contador


    alunos_com_altura_inferior = 0
    for i in range(10):
        if idades[i] > 13 and alturas[i] < media_alturas:
            alunos_com_altura_inferior += 1

    print("Quantidade de alunos com mais de 13 anos e altura inferior à média:", alunos_com_altura_inferior)
else:
    print("Não há alunos com mais de 13 anos para calcular a média.")
