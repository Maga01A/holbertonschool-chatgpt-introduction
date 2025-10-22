#!/usr/bin/python3
import sys

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
            Deposit money into the checkbook balance.

        Parameters:
            amount (float): Amount to deposit. Must be > 0.

        Returns:
            None
        """
        if amount <= 0:
            print("Deposit amount must be greater than $0.00.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
            Withdraw money from the checkbook balance if sufficient funds exist.

        Parameters:
            amount (float): Amount to withdraw. Must be > 0 and <= current balance.

        Returns:
            None
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than $0.00.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return
        self.balance -= amount
        print("Withdrew ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
            Print the current balance.

        Parameters:
            None

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def parse_amount(raw: str):
    """
    Safely parse a user-entered amount string into a float.

    Function description:
        Clean common formatting characters (commas, dollar sign, whitespace)
        and attempt to convert the value to float.

    Parameters:
        raw (str): The raw input string from the user.

    Returns:
        float: The parsed positive amount, or None if parsing failed.
    """
    if raw is None:
        return None
    s = raw.strip().replace(',', '').replace('$', '')
    if s == '':
        return None
    try:
        amount = float(s)
        return amount
    except ValueError:
        return None


def main():
    cb = Checkbook()
    try:
        while True:
            try:
                action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting.")
                break

            if action == 'exit':
                print("Goodbye.")
                break
            elif action == 'deposit':
                try:
                    raw = input("Enter the amount to deposit: $")
                except (EOFError, KeyboardInterrupt):
                    print("\nCanceled deposit.")
                    continue
                amount = parse_amount(raw)
                if amount is None:
                    print("Invalid amount. Please enter a numeric value (e.g., 100.00).")
                    continue
                cb.deposit(amount)
            elif action == 'withdraw':
                try:
                    raw = input("Enter the amount to withdraw: $")
                except (EOFError, KeyboardInterrupt):
                    print("\nCanceled withdrawal.")
                    continue
                amount = parse_amount(raw)
                if amount is None:
                    print("Invalid amount. Please enter a numeric value (e.g., 50.00).")
                    continue
                cb.withdraw(amount)
            elif action == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please enter: deposit, withdraw, balance, or exit.")
    except (EOFError, KeyboardInterrupt):
        # Catch any remaining interrupts and exit gracefully
        print("\nExiting.")
        sys.exit(0)


if __name__ == "__main__":
    main()
