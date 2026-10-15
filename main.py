from bank import Bank
from exceptions import BankingError


def show_menu():
    """Print the main menu."""
    print("\n===== Banking & Digital Wallet System =====")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. View statement")
    print("6. Exit")


def main():
    """Run the banking program."""
    bank = Bank("Python Bank")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            holder_name = input("Enter holder name: ")
            account_type = input("Enter account type (savings/checking/basic): ")
            try:
                account = bank.create_account(account_number, holder_name, account_type=account_type)
                print(f"Account {account.account_number} created for {account.holder_name}.")
            except BankingError as e:
                print("Error:", e)

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount_text = input("Enter amount to deposit: ")
            try:
                amount = float(amount_text)
                account = bank.get_account(account_number)
                account.deposit(amount)
                print(f"Deposited {amount:.2f}. New balance: {account.balance:.2f}")
            except BankingError as e:
                print("Error:", e)
            except ValueError:
                print("Error: Amount must be a number.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount_text = input("Enter amount to withdraw: ")
            try:
                amount = float(amount_text)
                account = bank.get_account(account_number)
                account.withdraw(amount)
                print(f"Withdrew {amount:.2f}. New balance: {account.balance:.2f}")
            except BankingError as e:
                print("Error:", e)
            except ValueError:
                print("Error: Amount must be a number.")

        elif choice == "4":
            from_number = input("Enter sender account number: ")
            to_number = input("Enter receiver account number: ")
            amount_text = input("Enter amount to transfer: ")
            try:
                amount = float(amount_text)
                bank.transfer(from_number, to_number, amount)
                source = bank.get_account(from_number)
                print(f"Transferred {amount:.2f}. Sender's new balance: {source.balance:.2f}")
            except BankingError as e:
                print("Error:", e)
            except ValueError:
                print("Error: Amount must be a number.")

        elif choice == "5":
            account_number = input("Enter account number: ")
            try:
                account = bank.get_account(account_number)
                lines = account.get_statement()
                print(f"\nStatement for {account.holder_name} ({account.account_number})")
                if not lines:
                    print("No transactions yet.")
                for line in lines:
                    print(line)
                print(f"Current balance: {account.balance:.2f}")
            except BankingError as e:
                print("Error:", e)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


main()