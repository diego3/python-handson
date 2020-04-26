from datetime import date


def obter_limite(salario, idade):
    return salario * (idade / 1000) + 100


def obter_idade(ano_nascimento):
    return date.today().year - ano_nascimento


def verificar_produto(produto, limite, idade):
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

    if len(nome_dono_loja) <= produto.preco <= idade:
        produto.desconto = len(nome_dono_loja.split(" ")[0])

    if produto.desconto > 0:
        print("voçê ganhou um desconto de {}, preco do produto {}".format(produto.desconto, produto.obter_preco()))


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


if __name__ == '__main__':
    nome_dono_loja = "Diego Rosa dos Santos"
    print("Bem vindo à loja do ", nome_dono_loja)
    print("Vamos realizar uma análise de crédito, para isso precisamos de alguns dados")
    cargo = input("qual o cargo que você trabalha?")
    salario = float(input("qual o seu salário?"))
    ano_nascimento = int(input("em que ano você nasceu?"))
    idade = obter_idade(ano_nascimento)
    print("os seguintes dados foram coletados")
    print("cargo:{}\nsalario:{:.2f}\nano de nascimento:{}\n".format(cargo, salario, ano_nascimento))
    print("idade = {}".format(idade))

    limite = obter_limite(salario, idade)

    print("você pode gastar até {:.2f}".format(limite))

    produto_quantidade_cadastro = int(input("quantos produtos você quer cadastrar?"))
    produtos_cadastrados = []
    while len(produtos_cadastrados) != produto_quantidade_cadastro:
        try:
            nome_produto = input("escreva o nome de um produto:")
            preco_produto = float(input("qual o preço do produto {}?:".format(nome_produto)))
            produto = Produto(nome_produto, preco_produto)

            verificar_produto(produto, limite, idade)

            produtos_cadastrados.append(produto)
        except LimiteException:
            print("Bloqueado, valor acima do seu limite")

    preco_total_produtos = sum(p.obter_preco() for p in produtos_cadastrados)
    if preco_total_produtos >= limite:
        print("Seu limite não permite comprar os cursos cadastrados")
    else:
        restante = limite - preco_total_produtos
        print("Saldo disponível do seu limite = {:.2f}".format(restante))