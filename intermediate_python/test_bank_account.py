import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bankaccount = BankAccount()

    def tearDown(self):
        self.bankaccount = None
        
    def test_initial_balance(self):
        self.assertEqual(self.bankaccount.balance, 100)

    def test_deposit_positive_amount(self):
        self.bankaccount.deposit(50)
        self.assertEqual(self.bankaccount.balance, 150)

if __name__ == "__main__":
    unittest.main()

    