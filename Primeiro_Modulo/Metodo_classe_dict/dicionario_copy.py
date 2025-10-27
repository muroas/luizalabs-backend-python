contatos = {
    "kauan@gmail.com": {"nome": "Kauan", "idade": 19}
}

copia_contatos = contatos.copy()
print(copia_contatos)

copia_contatos["kauan@gmail.com"] = {"nome": "Wallace"}

print(contatos)
print(copia_contatos)