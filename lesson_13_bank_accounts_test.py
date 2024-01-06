from lesson_13_bank_accounts import CreditAccount, CurrentAccount


class TestDepositFunds:
    def test_add_account_to_client(self, client, current_account):
        client.accounts.append(current_account)
        assert client.accounts

    def test_add_credit_account(self, client, credit_account):
        client.accounts.append(credit_account)
        assert len(client.accounts) == 2
        print(client.accounts)

    def test_deposit_on_current_on_1560(self, client):
        for account in client.accounts:
            if isinstance(account, CurrentAccount):
                account.deposit_money(1560)
                assert account.balance == 1560
                break

    def test_transfer_from_credit_to_debit(self, client):
        for account in client.accounts:
            if isinstance(account, CurrentAccount):
                cur_acc = account
                break
        for account in client.accounts:
            if isinstance(account, CreditAccount):
                cred_acc = account
                break

        cred_acc.make_transaction(cur_acc, 500)
        assert cur_acc.balance == 2060
        assert cred_acc.balance == (-500 - (500 * CreditAccount.percent_commission))

    def test_unsuccessfull_from_current_account(self, current_account, credit_account):
        print(current_account.__dict__)
        balance_before = current_account.balance
        current_account.make_transaction(credit_account, 50000000000)
        assert current_account.balance == balance_before

    def test_add_4_accounts_to_another_client(self, another_client, current_account, credit_account, current_account_2, credit_account_2):
        another_client.accounts.append(current_account)
        another_client.accounts.append(current_account_2)

        another_client.accounts.append(credit_account)
        another_client.accounts.append(credit_account_2)
        assert len(another_client.accounts) == 4
        print(another_client.accounts)

    def test_transfer_between_users(self, client, another_client, current_account, credit_account, current_account_2, credit_account_2):
        credit_account.deposit_money(1000)
        credit_account.make_transaction(current_account_2, 1.33)
        assert credit_account.balance
        assert current_account_2.balance
