"""Atividade 1"""

dicionario = {}

dicionario['chave1'] = 'valor1'
dicionario['chave2'] = 'valor2'
dicionario['chave3'] = 'valor3'

print("Elementos do dicionário:")
for chave, valor in dicionario.items():
    print(chave, ":", valor)

"""Atividade 2"""

mercado = {}

for i in range(3):
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    mercado[produto] = preco

print("Produtos no mercado:")
for produto, preco in mercado.items():
    print("Produto:", produto, "- Preço:", preco)

"""Ativiade 3"""

notas = []
for i in range(4):
    nota = float(input("Digite a nota {}: ".format(i + 1)))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média das notas:", media)

"""Atividade 4"""

caixa_misteriosa = []

for i in range(4):
    coisa = input("Digite uma coisa para colocar na Caixa Misteriosa: ")
    caixa_misteriosa.append(coisa)

numero = int(input("Digite um número (entre 0 e 3) para acessar a Caixa Misteriosa: "))

if 0 <= numero < len(caixa_misteriosa):
    print("Na posição", numero, "da Caixa Misteriosa tem:", caixa_misteriosa[numero])
else:
    print("Número fora do intervalo válido.")

"""Atividade 5"""

funcionarios = []

for i in range(3):
    nome = input("Digite o nome do funcionário {}: ".format(i + 1))
    funcionarios.append(nome)

print("Funcionários:")
for funcionario in funcionarios:
    print(funcionario)

demissao = input("Digite o nome do funcionário que deseja demitir: ")

if demissao in funcionarios:
    funcionarios.remove(demissao)
    print("Funcionário", demissao, "demitido.")
else:
    print("Funcionário não encontrado na lista.")

print("Funcionários restantes:")
for funcionario in funcionarios:
    print(funcionario)
