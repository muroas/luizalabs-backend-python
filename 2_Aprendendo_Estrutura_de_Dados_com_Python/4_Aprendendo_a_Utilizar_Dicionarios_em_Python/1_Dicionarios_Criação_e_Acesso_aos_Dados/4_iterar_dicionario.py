contatos = {
    "wallace@gmail.com": {"nome": "Wallace", "telefone": "99999-9999"},
    "kauan@gmail.com": {"nome": "Kauan", "telefone": "99999-9998"},
    "jorge@gmail.com": {"nome": "Jorge", "telefone": "99999-9997"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "99999-9996"},
}

for chave in contatos:
    print(chave, contatos[chave])

    print("=" * 60)

for chave, valor in contatos.items():
    print(chave, valor)