from app import criar_cliente, criar_conta, depositar, sacar, extrato, executar_transacao
import pytest

def setup_cliente_e_conta():
    cliente = criar_cliente("Rafael", "123", "01-01-2000", "Rua A")
    conta = criar_conta(cliente)
    return cliente, conta


def test_deposito():
    _, conta = setup_cliente_e_conta()
    assert depositar(conta, 100)
    assert conta["saldo"] == 100


def test_saque_valido():
    _, conta = setup_cliente_e_conta()
    depositar(conta, 200)
    assert sacar(conta, 50)
    assert conta["saldo"] == 150


def test_saque_invalido():
    _, conta = setup_cliente_e_conta()
    assert not sacar(conta, 50)


def test_extrato():
    _, conta = setup_cliente_e_conta()
    depositar(conta, 100)
    sacar(conta, 50)
    saida = extrato(conta)
    assert "Deposito" in saida
    assert "Saque" in saida
    assert "Saldo: R$ 50.00" in saida


def test_funcao_alta_ordem():
    _, conta = setup_cliente_e_conta()
    executar_transacao(depositar, conta, 300)
    assert conta["saldo"] == 300

