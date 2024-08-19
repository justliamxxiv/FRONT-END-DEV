# DEFINE THE CLASS FOR BANK ACCOUNTS
class BankAccount:
    def __init__(self, account_number: str, account_name: str, balance: float, pin: str):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.pin = pin

    def deposit(self, amount: float, pin: str) -> None:
      if pin == self.pin:
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
      else:
            print("Invalid PIN!")

    def withdraw(self, amount: float, pin: str) -> None:
      if pin == self.pin:
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
      else:
            print("Invalid PIN!")

    def check_balance(self, pin: str) -> None:
      if pin == self.pin:
        print(f"Current balance: ${self.balance}")
      else:
            print("Invalid PIN!")

    def send_money(self, recipient_account_number: str, amount: float, pin: str) -> None:
        if pin == self.pin:
            if amount > self.balance:
                print("Insufficient funds!")
            else:
                for account in accounts:
                    if account.account_number == recipient_account_number:
                        account.deposit(amount, account.pin)
                        self.balance -= amount
                        print(f"Sent ${amount} to account {recipient_account_number}. New balance: ${self.balance}")
                        return
                print("Recipient account not found!")
        else:
            print("Invalid PIN!")

# CREATE A LIST TO STORE BANK ACCOUNTS
accounts = []

# CREATE A NEW BANK ACCOUNT (Create account)
def create_account():
    account_number = input("Enter account number: ")
    account_name = input("Enter account name: ")
    balance = float(input("Enter initial balance: "))
    pin = input("Enter 4-digit PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("Invalid PIN! Please enter a 4-digit number.")
        return
    account = BankAccount(account_number, account_name, balance, pin)
    accounts.append(account)
    print("Account created successfully!")

# DESPOSIT MONEY INTO AN ACCOUNT (Deposit money)
def deposit_money():
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    pin = input("Enter PIN: ")
    for account in accounts:
        if account.account_number == account_number:
            account.deposit(amount, pin)
            return
    print("Account not found!")

# WITHDRAW MONEY FROM AN ACCOUNT (Withdraw money)
def withdraw_money():
    account_number = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    pin = input("Enter PIN: ")
    for account in accounts:
        if account.account_number == account_number:
            account.withdraw(amount, pin)
            return
    print("Account not found!")

# CHECK ACCOUNT BALANCE (Check account balance)
def check_balance():
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    for account in accounts:
        if account.account_number == account_number:
            account.check_balance(pin)
            return
    print("Account not found!")

# SEND MONEY TO ANOTHER ACCOUNT (Send money)
def send_money():
    sender_account_number = input("Enter your account number: ")
    recipient_account_number = input("Enter recipient's account number: ")
    amount = float(input("Enter amount to send: "))
    pin = input("Enter your PIN: ")
    for account in accounts:
        if account.account_number == sender_account_number:
            account.send_money(recipient_account_number, amount, pin)
            return
    print("Account not found!")

# MAIN PROGRAM LOOP
while True:
    print("1. Create account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Send money")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        send_money()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")