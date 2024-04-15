"""Atividade 1"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado

    def retornar_lado(self):
        return self.lado

    def calcular_area(self):
        return self.lado ** 2

quadrado1 = Quadrado(5)
print("Lado do quadrado:", quadrado1.retornar_lado())
print("Área do quadrado:", quadrado1.calcular_area())

quadrado1.mudar_lado(7)
print("Novo lado do quadrado:", quadrado1.retornar_lado())
print("Nova área do quadrado:", quadrado1.calcular_area())

"""Atividade 2"""

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)

def main():
    lado_a = float(input("Informe o comprimento do local em metros: "))
    lado_b = float(input("Informe a largura do local em metros: "))
    
    local = Retangulo(lado_a, lado_b)

    area_local = local.calcular_area()
    perimetro_local = local.calcular_perimetro()

    tamanho_piso = 1.0  # Em metros
    quantidade_pisos = area_local / tamanho_piso

    altura_rodape = 0.1  # Em metros
    comprimento_rodape = perimetro_local
    quantidade_rodapes = comprimento_rodape / altura_rodape

    print("\nPara o local com as medidas fornecidas:")
    print("Quantidade de pisos necessários:", int(quantidade_pisos))
    print("Quantidade de rodapés necessários:", int(quantidade_rodapes))

if __name__ == "__main__":
    main()

"""Atividade 3"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso_ganho):
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        self.altura += altura_ganha

    def retornar_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos, Peso: {self.peso} kg, Altura: {self.altura} cm"

pessoa1 = Pessoa("João", 18, 70, 170)
print("Informações da pessoa antes das mudanças:")
print(pessoa1.retornar_informacoes())

pessoa1.envelhecer()
pessoa1.engordar(5)
pessoa1.emagrecer(3)
print("\nInformações da pessoa após as mudanças:")
print(pessoa1.retornar_informacoes())

"""Ativida 4"""

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Novo saldo: R${self.saldo:.2f}")

conta1 = ContaCorrente("123456", "João da Silva")
print("Informações da conta:")
print("Número da conta:", conta1.numero_conta)
print("Nome do correntista:", conta1.nome_correntista)
print("Saldo:", conta1.saldo)

conta1.deposito(100)
conta1.saque(50)
conta1.alterarNome("João Oliveira")
print("\nInformações atualizadas da conta:")
print("Número da conta:", conta1.numero_conta)
print("Nome do correntista:", conta1.nome_correntista)
print("Saldo:", conta1.saldo)

"""Ativiade 5"""

class Televisor:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal inválido. O canal deve estar entre 1 e 100.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume máximo alcançado.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume mínimo alcançado.")

televisor = Televisor()

while True:
    print("\n1. Mudar de canal")
    print("2. Aumentar volume")
    print("3. Diminuir volume")
    print("4. Desligar o televisor")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_canal = int(input("Digite o número do canal desejado: "))
        televisor.mudar_canal(novo_canal)
    elif opcao == "2":
        televisor.aumentar_volume()
    elif opcao == "3":
        televisor.diminuir_volume()
    elif opcao == "4":
        print("Televisor desligado.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
