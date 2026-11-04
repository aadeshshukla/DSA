
class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")

    def menu(self):
        while True:
            print("\n===== SIMPLE BANKING SYSTEM =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                print("Thank you for using our bank!")
                break

            else:
                print("Invalid choice! Try again.")


# Main Program
print("Welcome to Python Bank!")

name = input("Enter account holder name: ")
account = Bank(name)

print(f"\nWelcome, {account.name}!")

account.menu()
