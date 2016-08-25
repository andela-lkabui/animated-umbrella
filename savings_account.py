from bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    Class representation of a SavingsAccount.

    Attributes:
        balance: Represents current account balance. Minimum amount is 500.
        deposit: This method contains logic to increment to the current account
                 balance.
        withdraw: This method contains logic to decrement to the current account
                 balance.
    """

    def __init__(self):
        """
        Constructor that sets initial balance to the minimum amount of 500.
        """
        self.balance = 500

    def deposit(self, amount):
        """
        Method to take in cash amounts and increment this to the current
        balance.
        """
        if amount < 0:
            return "Invalid deposit amount"
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Method to take in cash amounts and decrease this from the current
        balance.
        """
        if amount < 0:
            return "Invalid withdraw amount"
        elif (amount > self.balance):
            return "Cannot withdraw beyond the current account balance"
        elif (self.balance - amount) < 500:
            return "Cannot withdraw beyond the minimum account balance"
        else:
            self.balance -= amount
            return self.balance