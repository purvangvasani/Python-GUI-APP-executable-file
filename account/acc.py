class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount 

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking amount"""

    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

# account = Account('balance.txt')
# print(account.balance)
# account.withdraw(100)
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()

checking = Checking('balance.txt', 1)
print(checking.balance)
checking.transfer(100)
print(checking.balance)
print(checking.__doc__)
checking.commit()