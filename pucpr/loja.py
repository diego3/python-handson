from datetime import date


class AnaliseCredito:
    def __init__(self, cliente):
        self.cliente = cliente

    def obter_limite(self):
        return cliente.salario * (cliente.idade / 1.000) + 100


class CadastroProduto:
    def __init__(self, analise_credito, desconto):
        self.analise_credito = analise_credito
        self.desconto = desconto

    def cadastrar_massivo(self, quantidade):
        produtos_cadastrados = []
        limite = self.analise_credito.obter_limite()
        while len(produtos_cadastrados) != quantidade:
            try:
                nome_produto = Console().string("escreva o nome de um produto: ")
                preco_produto = Console().float("qual o preço do produto {}? : ".format(nome_produto))
                produto = Produto(nome_produto, preco_produto)
                self.verificar_produto(produto, limite)
                produtos_cadastrados.append(produto)
            except LimiteException:
                print("Bloqueado, valor acima do seu limite")
                sair = input("Continuar cadastrando? (s/n): ")
                if sair.upper() == "N":
                    break
        return produtos_cadastrados

    def verificar_produto(self, produto, limite):
        if produto.preco > limite:
            raise LimiteException()

        percentual_60 = limite * 0.6
        percentual_90 = limite * 0.9

        if produto.preco <= percentual_60:
            print("Liberado")
        elif percentual_60 <= produto.preco <= percentual_90:
            print("Liberado, você pode parcelar em até 2 vezes")
        elif percentual_90 <= produto.preco <= limite:
            print("Liberado, você pode parcelar em 3 ou mais vezes")

        if len(nome_dono_loja) <= produto.preco <= self.analise_credito.cliente.idade:
            produto.desconto = self.desconto
            print("voçê ganhou um desconto de R${:.2f}, preco do produto R${:.2f}".format(produto.desconto, produto.obter_preco()))


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.desconto = 0

    def obter_preco(self):
        if self.desconto > 0:
            return self.preco - self.desconto
        return self.preco


class LimiteException(Exception):
    pass


class Console:
    def __init__(self):
        self.valor = 0

    def float(self, pergunta):
        return self._validate(pergunta, "float")

    def integer(self, pergunta):
        return self._validate(pergunta, "integer")

    def string(self, pergunta):
        return self._validate(pergunta, "string")

    def _validate(self, pergunta, tipo):
        valor_capturado = False
        while valor_capturado is False:
            try:
                if tipo == "float":
                    self.valor = float(input(pergunta))
                elif tipo == "integer" or tipo == "int":
                    self.valor = int(input(pergunta))
                else:
                    self.valor = input(pergunta)
                valor_capturado = True
            except ValueError:
                print("Valor incorreto, utilize apenas números")
        return self.valor


class Cliente:
    def __init__(self, cargo, salario, ano_nascimento):
        self.cargo = cargo
        self.salario = salario
        self.ano_nascimento = ano_nascimento
        self.idade = date.today().year - self.ano_nascimento

    def __str__(self):
        str_template = "cargo:{}\nsalario:R${:.2f}\nano de nascimento:{}\nidade:{}\n"
        return str_template.format(self.cargo, self.salario, self.ano_nascimento, self.idade)


if __name__ == '__main__':
    nome_dono_loja = "Diego Rosa dos Santos"
    desconto = len(nome_dono_loja.split(" ")[0])

    print("Bem vindo à loja", nome_dono_loja)
    print("Vamos realizar uma análise de crédito, para isso precisamos de alguns dados")

    # coleta de dados do cliente
    cargo = Console().string("qual o cargo que você trabalha? ")
    salario = Console().float("qual o seu salário? ")
    ano_nascimento = Console().integer("em que ano você nasceu? ")
    cliente = Cliente(cargo, salario, ano_nascimento)
    print("os seguintes dados foram coletados")
    print(cliente)

    # análise de crédito do cliente
    analise_credito = AnaliseCredito(cliente)
    limite = analise_credito.obter_limite()
    print("Crédito liberado R${:.2f}".format(limite))

    # cadastro de produtos
    cadastro = CadastroProduto(analise_credito, desconto)
    quantidade = Console().integer("quantos produtos você quer cadastrar? ")
    produtos = cadastro.cadastrar_massivo(quantidade)

    # análise de crédito final para os produtos cadastrados
    preco_total_produtos = sum(p.obter_preco() for p in produtos)
    print("Preço total produtos R${:.2f}".format(preco_total_produtos))

    if preco_total_produtos >= limite:
        print("Seu crédito atual não permite adquirir estes produtos")
        print("Limite R${:.2f}".format(limite))
    else:
        restante = limite - preco_total_produtos
        print("Crédito disponível R${:.2f}".format(restante))
