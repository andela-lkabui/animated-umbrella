import unittest

from bank_account import BankAccount


class BankAccountTestCases(unittest.TestCase):
  
    def test_that_bank_account_class_has_withdraw_method(self):
        try:
            self.assertTrue(BankAccount.deposit)
        except AttributeError as ae:
            self.assertFalse(ae, msg="Method deposit has not been defined in BankAccount")

    def test_that_bank_account_class_has_deposit_method(self):
        try:
            self.assertTrue(BankAccount.withdraw)
        except AttributeError as ae:
            self.assertFalse(ae, msg="Method withdraw has not been defined in BankAccount")
