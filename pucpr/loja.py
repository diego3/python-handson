import datetime

# Mostre quanto o cliente poderá gastar na sua loja (o limite de gasto),
# calculado da seguinte forma: [salário x (idade / 1.000)] + 100.

if __name__ == '__main__':
    print("Bem vindo à loja do Diego R. dos Santos")
    print("Vamos realizar uma análise de crédito, para isso precisamos de alguns dados seu.")
    cargo = input("qual o cargo que você trabalha?")
    salario = float(input("qual o seu salário?"))
    ano_nascimento = int(input("em que ano você nasceu?"))
    hoje = datetime.date.today()
    print("os seguintes dados foram coletados")
    print("cargo:{}\nsalario:{:.2f}\nano de nascimento:{}\n".format(cargo, salario, ano_nascimento))
    idade = hoje.year - ano_nascimento
    divisao = idade / 1.000
    print("divisao", divisao)
    limite = salario * (idade / 1.000)
    print("idade = {}".format(idade))
    print("você pode gastar até {:.2f}".format(limite))
    print("você pode gastar até ", limite)
