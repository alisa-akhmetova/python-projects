class BankAccount:
    bank_name = "P Bank"
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    @classmethod
    def from_string(cls, s):
        name, bal = s.split(',')
        return cls(name.strip(), float(bal))

    def deposit(self, amount):
        if not self.validate_amount(amount): raise ValueError('bad amount')
        self.balance += amount

    def transfer(self, *accounts, amount):
        for acc in accounts:
            acc.deposit(amount)
        self.balance -= amount * len(accounts)

    def update(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __str__(self): return f"{self.owner}: {self.balance} eur"

#test
if __name__ == "__main__":
    a = BankAccount("Alisa", 100)
    b = BankAccount.from_string("Alina,500")
    a.transfer(b, amount=20)
    print(a, b)