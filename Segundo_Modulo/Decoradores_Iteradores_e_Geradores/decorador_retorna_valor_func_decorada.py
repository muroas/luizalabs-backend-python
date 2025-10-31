def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a funcção")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar a função")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")
    return nome.upper()

resultado = ola_mundo("Kauan")
print(resultado)
print(ola_mundo.__name__)
