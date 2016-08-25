import unittest

from bank_account import BankAccount
from savings_account import SavingsAccount


class TestSavingsAccount(unittest.TestCase):
    """Class to test the SavingsAccount class"""

    def setUp(self):
        self.sa = SavingsAccount()
    
    def tearDown(self):
        del self.sa

    def test_current_account_is_instance_of_bank_account(self):
        self.assertTrue(isinstance(self.sa, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')
  
    def test_savings_account_cannot_deposit_negative_amounts(self):
        message = self.sa.deposit(-500)
        self.assertEquals(message, 'Invalid deposit amount', msg='No negative deposits')

    def test_savings_account_can_deposit_valid_amounts(self):
        init_balance = self.sa.balance
        balance = self.sa.deposit(1500)
        self.assertEquals(balance, (1500 + init_balance), msg='Balance does not match deposit')

    def test_savings_account_cannot_withdraw_negative_amounts(self):
        message = self.sa.withdraw(-1500)
        self.assertEquals(message, 'Invalid withdraw amount', msg='Negative amount cannot be withdrawn')

    def test_savings_account_cannot_withdraw_more_than_current_balance(self):
        message = self.sa.withdraw(1500)
        self.assertEquals(message, 'Cannot withdraw beyond the minimum account balance', msg='No overdrafts')

    def test_savings_account_cannot_withdraw_more_than_minimum_balance(self):
        message = self.sa.withdraw(501)
        self.assertEquals(message, 'Cannot withdraw beyond the minimum account balance')

    def test_savings_account_can_withdraw_valid_amounts_successfully(self):
        self.sa.deposit(2300)
        self.sa.withdraw(543)
        self.assertEquals(2257, self.sa.balance, msg="Incorrect balance after withdrawal")
