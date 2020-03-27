from ponto.datatype import *

if __name__ == '__main__':
    # entrada = input("informe a entrada:")
    ref = "18/03/2020"
    ent = "18:00"
    sai = "18:15"
    mdt = MyDate(ref)
    print(mdt.is_valid())
    print(mdt.get_date())
    entrada = MyTime(ent)
    print(entrada.is_valid())
    print(entrada.get_val())
    saida = MyTime(sai)
    print(saida.is_valid())
    print(saida.get_val())
    print(saida.get_val() - entrada.get_val())
