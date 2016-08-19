import unittest

from bank_account import BankAccount
from current_account import CurrentAccount


class TestCurrentAccount(unittest.TestCase):
    """Class to test the CurrentAccount class"""

    def setUp(self):
        """
        Initializes state of TestCurrentAccount variables
        """
        self.ca = CurrentAccount()

    def tearDown(self):
        """
        Deletes state of TestCurrentAccount variables
        """
        del self.ca

    def test_current_account_is_instance_of_bank_account(self):
        """
        Tests that CurrentAccount creates an instance of BankAccount.
        """
        self.assertTrue(
            isinstance(self.ca, BankAccount),
            msg="CurrentAccount is not a subclass of BankAccount")

    def test_current_account_cannot_deposit_negative_amounts(self):
        """
        Tests that CurrentAccount cannot deposit negative cash amounts.
        """
        message = self.ca.deposit(-500)
        self.assertEquals(message, "Invalid deposit amount")

    def test_current_account_can_deposit_valid_amounts(self):
        """
        Tests that CurrentAccount can deposit valid cash amounts.
        """
        balance = self.ca.deposit(1500.63)
        self.assertEquals(balance, 1500.63)

    def test_current_account_cannot_withdraw_negative_amounts(self):
        """
        Tests that CurrentAccount cannot withdraw negative cash amounts.
        """
        message = self.ca.withdraw(-1500.63)
        self.assertEquals(message, "Invalid withdraw amount")

    def test_current_account_cannot_withdraw_more_than_current_balance(self):
        """
        Tests that CurrentAccount cannot withdraw more than current balance.
        (Current balance for newly created CurrentAccount is 0)
        """
        message = self.ca.withdraw(1500.63)
        self.assertEquals(
            message,
            "Cannot withdraw beyond the minimum account balance")    