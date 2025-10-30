import textwrap

def menu():
    opcao = input("""

    Selecione uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Usuário
    [cc] Criar Conta
    [lc] Listar Contas
    [q] Sair

    => """)

    return opcao

def depositar(saldo, valor, extrato, /):
        
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

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

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o número do CPF (somente número): ")
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe uma conta cadastrada com esse CPF!")
        return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro, bairro, cidade/sigla, estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("-== Usuário criado com sucesso ==-")

def verificar_usuario (cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None
    
def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF para iniciar: " )
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("\n ---=== Conta criada com sucesso! ===---")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("\n ---=== Usuário não encontrado, peço que entre em contato com seu gerente! ===---")

def listar_contas(contas):
    print(f"Quantidade de contas cadastradas: {len(contas)}")
    for conta in contas:
        linha = f"""
            Agência:\t\t{conta['agencia']}
            Número da conta:\t{conta['numero_conta']}
            Titular:\t\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "001"

    usuarios = []
    contas = []
    numero_conta = 1

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe um valor: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe um valor: "))
            saldo, extrato = saque(saldo=saldo, valor=valor, limite=limite, extrato="extrato", numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "c":
            criar_usuario(usuarios)

        elif opcao == "cc":
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
    