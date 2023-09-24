#### Bank Accounts

class BankAccounts():
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name     = first_name
        self.last_name      = last_name
        self.account_id     = account_id
        self.account_type   = account_type
        self.pin            = pin
        self.balance        = balance

    def deposit(self, x):
        self.balance = self.balance + x

    def withdraw(self, x):
        self.balance = self.balance - x

    def show_balance(self):
        print(f"Your balance is: £{self.balance}")
    
george = BankAccounts("George", "Turner", 1998, "Savings", 2002, 100.00)

print()
george.show_balance()

#george.deposit(1000)
george.deposit(x = float(input("\nHow much would you like to deposit? £")))

print()
george.show_balance()

#george.withdraw(999)
george.withdraw(x = float(input("\nHow much would you like to withdraw? £")))

print()
george.show_balance()

