MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

# Utilizando apenas if

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Utilizando else

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

# Utilizando elif

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")