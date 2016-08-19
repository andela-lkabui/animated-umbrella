import unittest

from bank_account import BankAccount
from savings_account import SavingsAccount


class TestSavingsAccount(unittest.TestCase):
    """Class to test the SavingsAccount class"""

    def setUp(self):
        """
        Initializes state of TestSavingsAccount variables
        """
        self.sa = SavingsAccount()

    def tearDown(self):
        """
        Deletes state of TestSavingsAccount variables
        """
        del self.sa

    def test_savings_account_is_instance_of_bank_account(self):
        """
        Tests that SavingsAccount creates an instance of BankAccount.
        """
        self.assertTrue(
            isinstance(self.sa, BankAccount),
            msg="SavingsAccount is not a subclass of BankAccount")

    def test_savings_account_cannot_deposit_negative_amounts(self):
        """
        Tests that SavingsAccount cannot deposit negative cash amounts.
        """
        message = self.sa.deposit(-500)
        self.assertEquals(message, "Invalid deposit amount")

    def test_savings_account_can_deposit_valid_amounts(self):
        """
        Tests that CurrentAccount can deposit valid cash amounts.
        """
        init_balance = self.sa.balance
        balance = self.sa.deposit(1500)
        self.assertEquals(balance, (1500 + init_balance))

    def test_savings_account_cannot_withdraw_negative_amounts(self):
        """
        Tests that SavingsAccount cannot withdraw negative cash amounts.
        """
        message = self.sa.withdraw(-1500)
        self.assertEquals(message, "Invalid withdraw amount")

    def test_savings_account_cannot_withdraw_more_than_current_balance(self):
        """
        Tests that SavingsAccount cannot withdraw more than current balance.
        (Current balance for newly created SavingsAccount is 500)
        """
        message = self.sa.withdraw(1500)
        self.assertEquals(
            message,
            "Cannot withdraw beyond the minimum account balance")

    def test_savings_account_cannot_withdraw_more_than_minimum_balance(self):
        """
        Tests that SavingsAccount cannot withdraw more than minimum balance.
        (Minimum balance for newly created SavingsAccount is 500)
        """
        message = self.sa.withdraw(501)
        self.assertEquals(
            message,
            "Cannot withdraw beyond the minimum account balance")

    def test_savings_account_can_withdraw_valid_cash_amounts(self):
        """
        Tests that SavingsAccount can withdraw valid cash amounts.
        """
        # deposit some money first
        self.sa.deposit(2300)
        # now withdraw
        self.sa.withdraw(543)
        self.assertEquals(
            2257, self.sa.balance, msg="Incorrect balance after withdrawal")