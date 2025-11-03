nome = "Kauan"
idade = 22
profissao = "Estagiário"
linguagem = "Python"

dados = {"nome": "Kauan", "idade": 22, "profissao": "Estagiário", "linguagem": "Python"}

print("Nome: {} Idade: {} Profissão: {} Linguagem: {}".format(nome, idade, profissao, linguagem))
print("Nome: {0} Idade: {1} Profissão: {2} Linguagem: {3}".format(nome, idade, profissao, linguagem))
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(**dados))