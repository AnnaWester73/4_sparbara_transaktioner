class BankAccount:
    def __init__(self, balance, logger):
        self.balance = balance
        self.logger = logger

    def deposit(self, amount):
        self.balance += amount
        self.logger.log(f"Insättning {amount}kr. Nytt saldo {self.balance}kr")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.logger.log(f"Uttag {amount}kr. Nytt saldo {self.balance}kr")
            return True
        else:
            self.logger.log(f"Du har inte tillräckligt på kontot. Saldo {self.balance}kr")
            return False