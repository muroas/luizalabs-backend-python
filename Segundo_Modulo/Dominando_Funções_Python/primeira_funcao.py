def exibir_mensagem ():
    print("Olá mundo!")

def exibir_mensagem_2 (nome):
    print(f"Seja bem vindo, {nome}!")

def exibir_mensagem_3 (nome="Desconhecido"):
    print(f"Seja bem vindo, {nome}!")

exibir_mensagem()
exibir_mensagem_2("Kauan")
exibir_mensagem_3()
exibir_mensagem_3("Wallace")