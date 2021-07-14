""" 
List of accounts
    functions access account by index position
create dict/map of act name and list index
prompt user for account name
    use map to populate index value for functions

nate.make_account(BankAccount("act01", 50))
def make_account(self, act_name):
        self.accounts.append(act_name)
        return self

"""


class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.accounts = []
        
    
    def make_account(self, act_name, balance=0, interest=0.01):
        self.accounts.append(BankAccount(act_name, balance, interest))
        return self
    
    def make_deposit(self, position, amount):
        self.accounts[position].deposit(amount)
        return self
    
    def make_withdrawal(self, position, amount):
        self.accounts[position].withdrawal(amount)
        return self

    def display_user_balance(self, position):
        print(f"Current balance for {self.name} account {self.accounts[position].name} is: {self.accounts[position].balance}")
        self.accounts[position].display_account_info()
        return self

    def transfer_money( self, position, person, p_position, amount):
        if amount <= self.accounts[position].balance:
            print(f"Current balance for  {self.name} account {self.accounts[position].name} is: {self.accounts[position].balance}")
            print(f"Current balance for  {person.name} account {person.accounts[position].name} is: {person.accounts[p_position].balance}")
            self.accounts[position].withdrawal(amount)
            person.accounts[p_position].deposit(amount) 
            print(f"Transfering {amount} from {self.name} {self.accounts[position].name} to {person.accounts[position].name} {person.name}")  
            print(f"Current balance for  {self.name} {self.accounts[position].name} is: {self.accounts[position].balance}")
            print(f"Current balance for  {person.name} {person.accounts[position].name} is: {person.accounts[p_position].balance}")
        else:
            print(f"Insufficient funds for transfer! Current balance is: {self.accounts[position].balance}")
        return self

class BankAccount():
    def __init__(self, act_name, balance=0, interest=0.01):
        self.balance = balance
        self.interest_rate = interest
        self.name = act_name

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance-= amount
        return self

    def display_account_info(self):
        print(f"Account Name: {self.name}")
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self


nate = User("Nate Langione", "nate@gmail.com")
john = User("John smith", "jsmith@gmail.com")
jane = User("Jane doe", "jdoe@gmail.com")

nate.make_account("act01", 10).make_account("act02", 0).make_deposit(0, 10).make_deposit(1, 20).make_withdrawal(0,10).display_user_balance(0).display_user_balance(1)
jane.make_account("act01", 100).transfer_money(0, nate, 0, 100)
john.make_account("act01", 150).make_account("act02", 30).make_deposit(0, 10).make_deposit(1, 50).make_withdrawal(0,2000).display_user_balance(0).display_user_balance(1)

#print(nate.__dict__)



