import pytest
from bank import BankAccount

@pytest.fixture
def account():
    print("\n[setup]")
    acc = BankAccount(100)
    yield acc
    print("\n[teardown]")

def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw(account):
    account.withdraw(40)
    assert account.balance == 60