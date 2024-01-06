import pytest
from lesson_13_bank_accounts import Client, CreditAccount, CurrentAccount


@pytest.fixture(scope='class')
def current_account() -> CurrentAccount:
    instance = CurrentAccount()
    return instance


@pytest.fixture(scope='class')
def current_account_2() -> CurrentAccount:
    instance = CurrentAccount()
    return instance


@pytest.fixture(scope='class')
def credit_account() -> CreditAccount:
    instance = CreditAccount(limit=-2000)
    return instance


@pytest.fixture(scope='class')
def credit_account_2() -> CreditAccount:
    instance = CreditAccount(limit=-2000)
    return instance

@pytest.fixture(scope='class')
def client() -> Client:
    instance = Client(name='Alex')
    return instance


@pytest.fixture(scope='class')
def another_client() -> Client:
    instance = Client(name='Bob')
    return instance
