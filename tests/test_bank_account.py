# Testfall 1
# Saldo 50 kr
# Insättning 100kr

# Testfall 2
# Saldo 100kr
# Uttag 20kr
# Return True
# Nytt saldo 80kr

# Testfall 3
# Saldo 100kr
# Uttag 150kr
# return False
# Loggning: Finns inte tillräcklig på kontot

from src.bankaccount import BankAccount

class LoggerSpy:
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)

def test_deposit_increase_balance_and_logs ():

    logger = LoggerSpy()
    account = BankAccount(50, logger)

    account.deposit(100)

    assert account.balance == 150
    assert logger.messages == ["Insättning 100kr. Nytt saldo 150kr"]


def test_withdraw_success_reduces_balance_and_logs():

    logger = LoggerSpy()
    account = BankAccount(100, logger)

    result = account.withdraw(20)

    assert result is True
    assert account.balance == 80
    assert logger.messages == ["Uttag 20kr. Nytt saldo 80kr"]


def test_withdraw_fail_and_logs():

    logger = LoggerSpy()
    account = BankAccount(100, logger)

    result = account.withdraw(150)

    assert result is False
    assert account.balance == 100
    assert logger.messages == ["Du har inte tillräckligt på kontot. Saldo 100kr"]

