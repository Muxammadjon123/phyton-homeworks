class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_line(self):
        return f"{self.account_number},{self.name},{self.balance}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        if len(parts) == 3:
            try:
                return Account(parts[0], parts[1], float(parts[2]))
            except:
                return None
        return None


class Bank:
    def __init__(self):
        self.accounts = {}
        self.file_name = "accounts.txt"
        self.load_from_file()

    def generate_account_number(self):
        number = 1001
        while str(number) in self.accounts:
            number += 1
        return str(number)

    def create_account(self, name, initial_deposit):
        try:
            if initial_deposit < 0:
                print(" Deposit must be positive.")
                return
            acc_num = self.generate_account_number()
            self.accounts[acc_num] = Account(acc_num, name, initial_deposit)
            self.save_to_file()
            print(f"\n Account created. Account Number: {acc_num}")
        except:
            print(" Error creating account.")

    def view_account(self, account_number):
        acc = self.accounts.get(account_number)
        if acc:
            print(f"\n Account Number: {acc.account_number}")
            print(f" Name: {acc.name}")
            print(f" Balance: ${acc.balance:.2f}")
        else:
            print("\n Account not found.")

    def deposit(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            try:
                if amount <= 0:
                    print("\n Amount must be positive.")
                else:
                    acc.balance += amount
                    self.save_to_file()
                    print(f"\n {amount:.2f} deposited. New Balance: {acc.balance:.2f}")
            except:
                print("\n Deposit failed.")
        else:
            print("\n Account not found.")

    def withdraw(self, account_number, amount):
        acc = self.accounts.get(account_number)
        if acc:
            try:
                if amount <= 0:
                    print("\n Amount must be positive.")
                elif amount > acc.balance:
                    print("\n Insufficient balance.")
                else:
                    acc.balance -= amount
                    self.save_to_file()
                    print(f"\n {amount:.2f} withdrawn. New Balance: {acc.balance:.2f}")
            except:
                print("\n Withdrawal failed.")
        else:
            print("\nAccount not found.")

    def save_to_file(self):
        try:
            with open(self.file_name, "w") as f:
                for acc in self.accounts.values():
                    f.write(acc.to_line())
        except:
            print("Failed to save data.")

    def load_from_file(self):
        try:
            with open(self.file_name, "r") as f:
                for line in f:
                    acc = Account.from_line(line)
                    if acc:
                        self.accounts[acc.account_number] = acc
        except:
            pass


def main():
    bank = Bank()
    while True:
        print("\n======= BANKING SYSTEM MENU =======")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Select an option (1–5): ")

        if choice == "1":
            name = input("Enter your name: ")
            try:
                deposit = float(input("Initial deposit amount: "))
                bank.create_account(name, deposit)
            except:
                print(" Invalid input.")
        elif choice == "2":
            acc_num = input("Enter your account number: ")
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = input("Enter your account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(acc_num, amount)
            except:
                print("Invalid amount.")
        elif choice == "4":
            acc_num = input("Enter your account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(acc_num, amount)
            except:
                print(" Invalid amount.")
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print(" Invalid option.")

if __name__ == "__main__":
    main()
