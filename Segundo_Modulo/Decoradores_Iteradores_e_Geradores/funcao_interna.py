def principal():
    print("Executando a função princial")

    def funcao_intera():
        print("Executando a função interna")

    def funcao_2():
        print("Executando a função 2")

    funcao_intera()
    funcao_2()

principal()