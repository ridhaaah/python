class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    # Display account details
    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self.account_number}")
        print(f"Name           : {self.name}")
        print(f"Account Type   : {self.account_type}")
        print(f"Balance        : {self.balance}")


# Example Usage
acc = BankAccount("12345", "John Doe", "Savings", 1000)

acc.display()
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)  # Testing insufficient balance
acc.display()
