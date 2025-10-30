AGENCIA = "0001"
LIMITE_SAQUES = 500.0

# Opções de Menu

def menu_inicial():
    opcao = input("""
    --== Seja bem vindo ao nosso banco! ==--
                  
    Para iniciar, selecione uma opção:
                  
    [1] Criar Usuário
    [2] Criar Conta Corrente
    [3] Acessar Conta Corrente
    [0] Sair
    
    => """)

    return opcao

def menu_conta_corrente(conta):
    extrato = ""
    numero_saques = 0
    limite = 500.0

    while True:

        opcao_conta = input("""
        Selecione uma opção:

        [1] Realizar Deposito
        [2] Realizar Saque
        [3] Consultar Extrato
        [0] Sair
                            
        => """)

        if opcao_conta == "1":
            print("\n", "=" * 100, "\n")
            valor = float(input("Digite o valor a ser depositado na conta: "))
            conta["saldo"], extrato = depositar(conta["saldo"], valor, extrato)
        
        elif opcao_conta == "2":
            print("\n", "=" * 100, "\n")
            valor = float(input("Informe um valor: "))
            conta["saldo"], extrato = saque(saldo=conta["saldo"], valor=valor, limite=limite, extrato=extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao_conta == "3":
            exibir_extrato(conta["saldo"], extrato=extrato)
        
        elif opcao_conta == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Criação de Usuário

def criar_usuario(usuarios):
    print("=" * 100, "\n")
    cpf = input("Informe o número do CPF (somente número): ")
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("\tJá existe uma conta cadastrada com esse CPF!")
        return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro, bairro, cidade/sigla, estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n-== Usuário criado com sucesso ==-\n")
    print("=" * 100)

def verificar_usuario (cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

# Criação de Conta Corrente
  
def criar_conta_corrente(agencia, numero_conta, usuarios):
    print("=" * 100, "\n")
    cpf = input("Digite o CPF para iniciar: " )
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:

        print("\n--== Conta criada com sucesso! ==--\n")
        print("=" * 100)
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0.0}
    
    else:
        print("\n--== Usuário não encontrado, peço que entre em contato com seu gerente! ===---\n")

    print("=" * 100)

# Login da conta

def login_conta(contas, usuarios):
    print("\n", "=" * 100, "\n")
    agencia = input("Digite sua agência (ex: 0001): ")
    cpf = input("Digite seu CPF (apenas números): ")
    print("\n", "=" * 100)
    
    conta_encontrada = None

    for conta in contas:
        if conta["agencia"] == agencia and conta["usuario"]["cpf"] == cpf:
            conta_encontrada = conta
            break

    if conta_encontrada:
        print(f"\n\tSeja bem vindo, {conta_encontrada["usuario"]["nome"]}!")
        menu_conta_corrente(conta_encontrada)
    
    else:
        print("\n", "Agência ou CPF incorretos!", "\n")
        print("=" * 100)

# Funções de Deposito, Saque e Extrato

def depositar(saldo, valor, extrato, /):
        
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"--== Deposito no valor de R${valor} realizado com sucess! ==--")
    else:
        print("Operação falhou! O valor informado é inválido.")

    print("\n", "=" * 100, "\n")

    return saldo, extrato

def saque(*, saldo, valor, limite, extrato, numero_saques, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"--== Saque no valor de R${valor} realizado com sucess! ==--")

    else:
        print("Operação falhou! O valor informado é inválido.")

    print("\n", "=" * 100)

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n", "=" * 100, "\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n", "=" * 100)

# Main

def main():

    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        opcao = menu_inicial()
        
        if opcao == "1":
            criar_usuario(usuarios)
        
        elif opcao == "2":
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "3":
            login_conta(contas, usuarios)
        
        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()
