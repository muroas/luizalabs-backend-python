contatos = {"kauan@gmail.com": {"nome": "Kauan", "idade": 19}}

# contatos["chave"] # KeyError

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get("kauan@gmail.com", {})
print(resultado)

contatos2 = {"nome": "Kauan", "idade": 19}

print(contatos.get(1))