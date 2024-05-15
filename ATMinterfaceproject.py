class ATM:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def display_menu(self):
        print("\nATM Menu:")
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Quit")

    def view_balance(self):
        print("Your current balance is:",self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. Current balance is {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")
        print(f"Deposited {amount}. Current balance is {self.balance}")

    def view_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def run(self):
        print("Welcome to the ATM!")
        entered_user_id = input("Enter User ID: ")
        entered_pin = input("Enter PIN: ")
        if entered_user_id == self.user_id and entered_pin == self.pin:
            print("Authentication successful!")
            while True:
                self.display_menu()
                choice = input("Enter your choice (1-5): ")
                if choice == '1':
                    self.view_balance()
                elif choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    self.deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter withdraw amount: "))
                    self.withdraw(amount)
                elif choice == '4':
                    self.view_transaction_history()
                elif choice == '5':
                    print("Thank you for using the ATM!")
                    break
                else:
                    print("Invalid choice! Please try again.")
        else:
            print("Authentication failed! Invalid User ID or PIN.")
                  
atm = ATM("123456","98765")
atm.run()