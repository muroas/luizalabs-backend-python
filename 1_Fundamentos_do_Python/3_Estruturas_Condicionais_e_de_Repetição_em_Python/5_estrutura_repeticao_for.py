texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

#Exemplo com iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #adiciona uma quebra de linha

#Exemplo com range()
for numero in range(0, 51, 5):
    print(numero, end=" ")