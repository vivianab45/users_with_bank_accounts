class BankAccount:

    def __init__(self, int_rate, balance=0): 
        self.int_rate=int_rate
        self.balance=balance


    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance <amount:
            print(f"Insufficient funds: deduct $5 fee")
            self.balance-= 5
        self.balance -= amount
        return self
    def display_account_info(self):
        print (f"Balance:${self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)
        return self
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self



    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
        
    def display_user_balance (self,amount):
        self.account.display_account_info(amount)
        return self


        

account1=BankAccount(0.2,300)
account2=BankAccount(0.1,500)


# account1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
# account2.deposit(1000).deposit(500).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()


user1=User("Bob", "bob1@gmail.com")

user2=User("Susan", "susan2@gmail.com")

user1.make_deposit(100)

print(user1.name)


