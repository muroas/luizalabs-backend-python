contatos = {
    "kauan@gmail.com": {"nome": "Kauan", "idade": 19},
    "wallace@gmail.com": {"nome": "Wallace", "idade": 22}
}

resultado = "kauan@gmail.com" in contatos
print(resultado)

resultado = "jorge@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["wallace@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["wallace@gmail.com"]
print(resultado)
