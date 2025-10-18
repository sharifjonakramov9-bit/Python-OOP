import sys

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.is_active = False
        

    def deposit(self):
        amount = input("To take amount: ").strip()

        if not amount.isdigit():
            print("You must enter int")
            return

        amount = int(amount)
        self.balance += amount
        print(f"Your balance: {self.balance}")


    def withdraw(self):
        amount = input("To take amount: ").strip()

        if not amount.isdigit():
            print("You must enter int")
            return

        amount = int(amount)
        if amount <= self.balance:
            self.balance -= amount
            print(f"Your balance: {self.balance}!")
        else:
            print("Not enough balance!")


    def show_balance(self):
        print(f"Your current balance is {self.balance}$") 
    
def main(account):
    while True:
            print("""
            1.Deposit
            2.Withdraw
            3.check balance
            0.exit
            """)

            choice = input("Choice (0-3): ").strip()
            if choice == "1":
                account.deposit() 
            elif choice == "2":
                account.withdraw() 
            elif choice == "3":
                account.show_balance() 
            elif choice == "0":
                print("system closed")
                sys.exit() 
            else:
                print("You cannot choice this command please try again")



account = BankAccount("Jasur", 100)
main(account)
