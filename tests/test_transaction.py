# Test 1
# Saldo konto 1 100kr
# Saldo konto 2 50kr
# Överför 20kr från Konto A till konto B
# Nytt saldo konto A 80kr
# Nytt saldo konto B 70kr

# Test 2
# Saldo konto 1 100kr
# Saldo konto 2 50kr
# Överför 120kr från Konto 1 till konto 2
# Överföring kan inte genomföras mellan konton

from src.bankaccount import BankAccount
from src.transaction import Transaction

class LoggerSpy:
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)

def test_transfer_success_move_money_and_logs():
    logger = LoggerSpy()
    account1 = BankAccount(100, logger)
    account2 = BankAccount(50, logger)

    Transaction.transfer(20, account1, account2)

    assert account1.balance == 80
    assert account2.balance == 70

    assert logger.messages == ["Uttag 20kr. Nytt saldo 80kr", "Insättning 20kr. Nytt saldo 70kr"]


def test_transfer_fail_move_money_and_logs():
    logger = LoggerSpy()
    account1 = BankAccount(100, logger)
    account2 = BankAccount(50, logger)

    Transaction.transfer(120, account1, account2)

    assert account1.balance == 100
    assert account2.balance == 50

    assert logger.messages == ["Du har inte tillräckligt på kontot. Saldo 100kr"]