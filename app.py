import textwrap
from datetime import datetime


# ======== FUNÇÕES DE SUPORTE ========
def gerar_numero_conta():
    """Closure para gerar número sequencial de conta"""
    numero = 0
    def proximo():
        nonlocal numero
        numero += 1
        return numero
    return proximo

gerador_conta = gerar_numero_conta()


def criar_cliente(nome, cpf, data_nascimento, endereco):
    return {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "contas": []
    }


def criar_conta(cliente):
    conta = {
        "numero": gerador_conta(),
        "saldo": 0,
        "agencia": "0001",
        "cliente": cliente,
        "historico": []
    }
    cliente["contas"].append(conta)
    return conta


def registrar_transacao(conta, tipo, valor):
    conta["historico"].append({
        "tipo": tipo,
        "valor": valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })


# ======== TRANSAÇÕES ========
def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        registrar_transacao(conta, "Deposito", valor)
        return True
    return False


def sacar(conta, valor, limite=500, limite_saques=3):
    saques_realizados = len([t for t in conta["historico"] if t["tipo"] == "Saque"])

    if valor <= 0 or valor > conta["saldo"]:
        return False
    if valor > limite:
        return False
    if saques_realizados >= limite_saques:
        return False

    conta["saldo"] -= valor
    registrar_transacao(conta, "Saque", valor)
    return True


# ======== FUNÇÕES FUNCIONAIS ========
def executar_transacao(funcao_transacao, conta, valor):
    """Função de alta ordem: recebe como parâmetro a função de transação"""
    return funcao_transacao(conta, valor)


filtrar_cliente = lambda cpf, clientes: next((c for c in clientes if c["cpf"] == cpf), None)  # função lambda


def extrato(conta):
    transacoes = conta["historico"]
    if not transacoes:
        return "Não foram realizadas movimentações."
    # list comprehension
    return "\n".join([f"{t['tipo']}: R$ {t['valor']:.2f}" for t in transacoes]) + f"\nSaldo: R$ {conta['saldo']:.2f}"


# ======== MENU INTERATIVO ========
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    clientes, contas = [], []

    while True:
        opcao = menu()

        if opcao == "nu":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            nasc = input("Data nasc (dd-mm-aaaa): ")
            end = input("Endereço: ")
            clientes.append(criar_cliente(nome, cpf, nasc, end))
            print("Cliente criado com sucesso!")

        elif opcao == "nc":
            cpf = input("CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)
            if cliente:
                conta = criar_conta(cliente)
                contas.append(conta)
                print("Conta criada com sucesso!")
            else:
                print("Cliente não encontrado!")

        elif opcao == "d":
            cpf = input("CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)
            if cliente and cliente["contas"]:
                conta = cliente["contas"][0]
                valor = float(input("Valor depósito: "))
                executar_transacao(depositar, conta, valor)
            else:
                print("Cliente/conta não encontrado.")

        elif opcao == "s":
            cpf = input("CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)
            if cliente and cliente["contas"]:
                conta = cliente["contas"][0]
                valor = float(input("Valor saque: "))
                executar_transacao(sacar, conta, valor)
            else:
                print("Cliente/conta não encontrado.")

        elif opcao == "e":
            cpf = input("CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)
            if cliente and cliente["contas"]:
                conta = cliente["contas"][0]
                print(extrato(conta))
            else:
                print("Cliente/conta não encontrado.")

        elif opcao == "q":
            break


if __name__ == "__main__":
    main()
