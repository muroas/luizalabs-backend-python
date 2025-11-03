def verificador_ano_bissexto():
    ano = int(input())

    if ano % 4 == 0:
        print("SIM")
    
    elif ano % 100 != 0:
        print("NÃO")

    elif ano % 400 == 0:
        print("SIM")

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:

verificador_ano_bissexto()