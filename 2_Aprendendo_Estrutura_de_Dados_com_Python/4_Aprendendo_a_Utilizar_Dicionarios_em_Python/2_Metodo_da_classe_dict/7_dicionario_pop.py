contatos = {
    "kauan@gmail.com": {"nome": "Kauan", "idade": 19}
}

resultado = contatos.pop("kauan@gmail.com")
print(resultado)

resultado = contatos.pop("kauan@gmail.com", {})
print(resultado)
resultado = contatos.pop("kauan@gmail.com", "Não encontrado")
print(resultado)