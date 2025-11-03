def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retira seu dinheiro na boca do caixa.")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    print("Depósito realizado com sucesso!")
    print(f"Seu novo saldo é: {saldo}")

sacar(100)
depositar(200)