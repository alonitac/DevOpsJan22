"""
Create a bank account class that has two attributes:

* owner
* balance

and two methods:

* deposit
* withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account:

    currency = '$'

    def __init__(self, name, balance):
        self.owner = name
        self.balance = balance
        self.is_active = True

    def __str__(self):
        return 'Account owner: ' + self.owner + '\n' + \
               'Account balance: $' + str(self.balance)

    def __add__(self, other):
        if not isinstance(other, Account):
            print('Bad operation')
            return

        total = self.balance + other.balance
        self.balance = 0
        other.balance = 0
        self.is_active = False
        other.is_active = False
        return Account(self.owner + ' and ' + other.owner, total)

    def delete(self):
        print('Deleting your account...')

    def deposit(self, cash):
        if not (isinstance(cash, int) and cash > 0):
            print('Deposit Denied')
            return

        self.balance += cash
        print('Deposit Accepted')

    def withdraw(self, amount):
        if not isinstance(amount, int):
            print('Withdrawal Denied')
        elif not (0 < amount < self.balance):
            print('Funds Unavailable!')
        else:
            self.balance -= amount
            print(f'Withdrawal Accepted. Current balance: {self.balance}')


class StudentAccount(Account):
    def __init__(self, name, balance, uni, withdrawal_th=100):
        super().__init__(name, balance)
        self.withdrawal_th = withdrawal_th
        self.uni = uni

    def delete(self):
        print('Deletion denied')

    def withdraw(self, amount):
        if amount > self.withdrawal_th:
            print('Withdrawal is limited to 100$')
        else:
            super().withdraw(amount)


if __name__ == '__main__':

    # 1. Instantiate the class
    acct1 = Account('Jose', 100)
    acct2 = Account('Jose', 1000)

    print(acct1.owner)
    print(acct2.owner)

    print(acct1.currency)
    print(acct2.currency)

    acct1.owner = 'John'
    Account.currency = '!'

    print(acct1.owner)
    print(acct2.owner)

    print(acct1.currency)
    print(acct2.currency)

    acct2.withdraw(100)
    acct2.withdraw(150)
    # joint_account = acct1 + acct2

    # 2. Print the object
    print(acct1)
    # output:
    # >> Account owner:   Jose
    # >> Account balance: $100

    # 3. Show the account owner attribute
    print(acct1.owner)
    # >> 'Jose'

    # 4. Show the account balance attribute
    print(acct1.balance)
    # >> 100

    # 5. Make a series of deposits and withdrawals
    acct1.deposit(50)
    # >> Deposit Accepted

    acct1.withdraw(75)
    # Withdrawal Accepted

    # 6. Make a withdrawal that exceeds the available balance
    acct1.withdraw(500)
    # Funds Unavailable!


