from abc import ABCMeta, abstractmethod


class BankAccount(object):
    """
    Abstract BankAccount to be inherited by SavingsAccount and CurrentAccout.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def deposit(amount):
        """Takes in cash amount and increments it to the current balance."""

    @abstractmethod
    def withdraw(amount):
        """Takes in cash amount and decreases it from the current balance."""