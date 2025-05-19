class Bank :
    bank_name = "National bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

account1 = Bank()

print("Original Bank Name:", Bank.bank_name)
Bank.change_bank_name("state bank")
print(account1.bank_name)