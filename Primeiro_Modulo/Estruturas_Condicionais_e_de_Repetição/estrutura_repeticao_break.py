while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break #Vai parar o laço

    if numero % 2 == 0:
        continue #Vai pular a execução

    print(numero)

# for numero in range(100):
#     if numero % 2 == 0:
#         continue #Vai pular a execução

#     print(numero, end=" ")