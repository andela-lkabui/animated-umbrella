import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    """Class to test the BankAccount class"""

    def test_that_bank_account_class_is_abstract(self):
        """
        Tests that BankAccount class is abstract and cannot be instantiated.
        """
        with self.assertRaises(TypeError):
            BankAccount()
        with self.assertRaisesRegexp(TypeError, "Can't instantiate abstract class BankAccount with abstract methods deposit, withdraw"):
            BankAccount()

    def test_that_bank_account_class_has_withdraw_method(self):
        """
        Tests that BankAccount class has a withdraw method.
        """
        try:
            self.assertTrue(BankAccount.deposit)
        except AttributeError as ae:
            self.assertFalse(
                ae,
                msg="Virtual method deposit has not been defined in BankAccount")

    def test_that_bank_account_abstract_class_has_deposit_virtual_method(self):
        """
        Tests that BankAccount class has a deposit method.
        """
        try:
            self.assertTrue(BankAccount.withdraw)
        except AttributeError as ae:
            self.assertFalse(
                ae,
                msg="Virtual method withdraw has not been defined in BankAccount")

    def test_that_withdraw_and_deposit_are_abstract_methods(self):
        """
        Tests that BankAccount class has abstract methods *deposit* and
        *withdraw*
        """
        self.assertTrue('deposit' in BankAccount.__abstractmethods__)
        self.assertTrue('withdraw' in BankAccount.__abstractmethods__)