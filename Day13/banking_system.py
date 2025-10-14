# bank_oop_intermediate.py
# -----------------------------------------
# Intermediate OOP Banking System (Monthly interest = 5%)
# Concepts used:
# - Abstraction (abstract base class BankAccount)
# - Inheritance (SavingsAccount, CurrentAccount)
# - Encapsulation (private balance: __balance)
# - Polymorphism (override withdraw / apply_interest)
# - Transaction history, input validation
# -----------------------------------------

from abc import ABC, abstractmethod
from typing import Dict, List
import datetime

# ---------------------------
# Abstract base class (Abstraction)
# ---------------------------
class BankAccount(ABC):
    """
    Abstract base class that defines the interface and shared behavior
    for all account types.
    """
    def __init__(self, owner: str, initial_deposit: float = 0.0):
        # public attribute: account owner name
        self.owner = owner

        # private attribute: balance (encapsulated)
        # use double underscore to make name-mangled attribute __balance
        self.__balance = float(initial_deposit)

        # public attribute: simple transaction history list (strings)
        self.transactions: List[str] = []
        if initial_deposit > 0:
            # record initial deposit in transaction history with timestamp
            self.transactions.append(self._record_txn(f"Initial deposit: {initial_deposit}"))

        # store account creation date/time
        self.created_at = datetime.datetime.now()

    # Protected helper: format a transaction string with timestamp
    def _record_txn(self, desc: str) -> str:
        """Return a string with timestamp and description for the transaction log."""
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{ts}] {desc}"

    # Encapsulation: getter for balance (no direct write access)
    def get_balance(self) -> float:
        """Return the current balance (read-only access)."""
        return self.__balance

    # Encapsulation: internal method to change balance
    # kept protected (single underscore) to discourage direct use outside class hierarchy
    def _change_balance(self, amount: float):
        """Add (or subtract) amount to the private balance and return new balance."""
        self.__balance += amount
        return self.__balance

    # Common method: deposit money (shared behavior)
    def deposit(self, amount: float) -> bool:
        """
        Deposit money into account.
        Returns True on success, False on invalid input.
        """
        if amount <= 0:
            # invalid deposit amount
            return False
        new_balance = self._change_balance(amount)  # modify private balance safely
        self.transactions.append(self._record_txn(f"Deposited: {amount:.2f}. Balance: {new_balance:.2f}"))
        return True

    # Abstract withdraw method - must be implemented/overridden by subclasses
    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from account.
        Subclasses implement specific rules (e.g., min balance, fees).
        Should return True on successful withdrawal, False otherwise.
        """
        pass

    # Abstract method to apply interest (if any) - subclasses implement
    @abstractmethod
    def apply_monthly_interest(self):
        """
        Apply monthly interest or account-specific monthly operation.
        For accounts without interest, this can be a no-op in subclass.
        """
        pass

    # Show transaction history (user-facing)
    def show_transactions(self):
        """Print the transaction history line by line."""
        if not self.transactions:
            print("No transactions yet.")
            return
        print(f"Transaction history for {self.owner}:")
        for t in self.transactions:
            print(" ", t)

    # Utility: show basic account info
    def info(self):
        """Print basic account information."""
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.get_balance():.2f}")
        print(f"Created at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")


# ---------------------------
# Savings Account (inherits BankAccount)
# ---------------------------
class SavingsAccount(BankAccount):
    """
    Savings account that earns monthly interest.
    Monthly interest rate is stored per-instance (e.g., 0.05 for 5%).
    """
    def __init__(self, owner: str, initial_deposit: float = 0.0, monthly_interest_rate: float = 0.05):
        # call base class constructor
        super().__init__(owner, initial_deposit)
        # monthly interest rate (e.g., 0.05 == 5% per month)
        self.monthly_interest_rate = float(monthly_interest_rate)

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw from savings only if sufficient balance.
        No overdraft allowed.
        """
        if amount <= 0:
            # invalid amount
            return False
        current_balance = self.get_balance()
        if amount > current_balance:
            # not enough funds
            self.transactions.append(self._record_txn(f"Failed withdrawal attempt: {amount:.2f} (Insufficient funds)"))
            return False
        # perform withdrawal
        new_balance = self._change_balance(-amount)
        self.transactions.append(self._record_txn(f"Withdrew: {amount:.2f}. Balance: {new_balance:.2f}"))
        return True

    def apply_monthly_interest(self):
        """
        Calculate interest on current balance and credit it.
        Interest = balance * monthly_interest_rate
        """
        balance = self.get_balance()
        if balance <= 0:
            # nothing to apply interest to
            return
        interest = balance * self.monthly_interest_rate
        new_balance = self._change_balance(interest)
        self.transactions.append(self._record_txn(f"Interest credited: {interest:.2f}. Balance: {new_balance:.2f}"))
        # return interest amount for possible reporting
        return interest


# ---------------------------
# Current Account (inherits BankAccount)
# ---------------------------
class CurrentAccount(BankAccount):
    """
    Current account typically does not earn interest but may require minimum balance.
    We'll implement a minimum balance rule and a fee if withdrawal would drop below minimum.
    """
    def __init__(self, owner: str, initial_deposit: float = 0.0, minimum_balance: float = 100.0, below_min_fee: float = 10.0):
        super().__init__(owner, initial_deposit)
        # minimum required balance
        self.minimum_balance = float(minimum_balance)
        # fee charged if balance falls below minimum after a withdrawal
        self.below_min_fee = float(below_min_fee)

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw with check for minimum balance.
        If withdrawal causes balance < minimum_balance, apply fee (if possible).
        Disallow withdrawal if insufficient funds for both amount + fee.
        """
        if amount <= 0:
            return False
        balance = self.get_balance()
        # if withdrawal amount is greater than current balance -> fail
        if amount > balance:
            self.transactions.append(self._record_txn(f"Failed withdrawal attempt: {amount:.2f} (Insufficient funds)"))
            return False

        # simulate balance after withdrawal
        new_balance = balance - amount

        if new_balance < self.minimum_balance:
            # decide whether we can charge fee
            total_needed = amount + self.below_min_fee
            if total_needed > balance:
                # cannot cover withdrawal + fee
                self.transactions.append(self._record_txn(f"Failed withdrawal attempt: {amount:.2f} (Would breach min balance and cannot pay fee)"))
                return False
            else:
                # allow withdrawal then apply fee
                self._change_balance(-amount)  # withdraw amount
                # apply fee
                self._change_balance(-self.below_min_fee)
                self.transactions.append(self._record_txn(f"Withdrew: {amount:.2f}. Fee charged: {self.below_min_fee:.2f}. Balance: {self.get_balance():.2f}"))
                return True
        else:
            # normal withdrawal, no fee
            self._change_balance(-amount)
            self.transactions.append(self._record_txn(f"Withdrew: {amount:.2f}. Balance: {self.get_balance():.2f}"))
            return True

    def apply_monthly_interest(self):
        """
        CurrentAccount doesn't earn interest in this model. We implement as no-op,
        but this method exists to honor the abstract interface and support polymorphism.
        """
        # no interest: return 0 to indicate nothing was applied
        return 0.0


# ---------------------------
# Simple Bank Manager: handle multiple accounts
# ---------------------------
class BankManager:
    """
    A small helper class to manage multiple accounts in memory.
    It demonstrates using the account classes in a realistic flow.
    """
    def __init__(self):
        # dictionary mapping account numbers (str) to account objects
        self.accounts: Dict[str, BankAccount] = {}
        # auto-increment simple account id starting from 2001
        self._next_acc_num = 2001

    def _generate_acc_num(self) -> str:
        """Generate a new account number as string."""
        acc = str(self._next_acc_num)
        self._next_acc_num += 1
        return acc

    def create_savings(self, owner: str, initial_deposit: float = 0.0, monthly_interest_rate: float = 0.05) -> str:
        """Create a SavingsAccount and return its account number."""
        acc_num = self._generate_acc_num()
        account = SavingsAccount(owner, initial_deposit, monthly_interest_rate)
        self.accounts[acc_num] = account
        account.transactions.append(account._record_txn(f"Account created: SavingsAccount {acc_num}"))
        return acc_num

    def create_current(self, owner: str, initial_deposit: float = 0.0, minimum_balance: float = 100.0, below_min_fee: float = 10.0) -> str:
        """Create a CurrentAccount and return its account number."""
        acc_num = self._generate_acc_num()
        account = CurrentAccount(owner, initial_deposit, minimum_balance, below_min_fee)
        self.accounts[acc_num] = account
        account.transactions.append(account._record_txn(f"Account created: CurrentAccount {acc_num}"))
        return acc_num

    def get_account(self, acc_num: str) -> BankAccount:
        """Return account object or raise KeyError if not found."""
        if acc_num not in self.accounts:
            raise KeyError("Account not found")
        return self.accounts[acc_num]

    def deposit_to(self, acc_num: str, amount: float) -> bool:
        """Deposit into specified account number. Returns True if success."""
        account = self.get_account(acc_num)
        success = account.deposit(amount)
        return success

    def withdraw_from(self, acc_num: str, amount: float) -> bool:
        """Withdraw from specified account using polymorphic withdraw implementation."""
        account = self.get_account(acc_num)
        success = account.withdraw(amount)
        return success

    def apply_monthly_interest_all(self):
        """
        Apply monthly interest (or monthly operations) to all accounts.
        Uses polymorphism: SavingsAccount applies interest; CurrentAccount does nothing.
        """
        interest_report = {}
        for acc_num, acc in self.accounts.items():
            interest = acc.apply_monthly_interest()
            interest_report[acc_num] = interest
        return interest_report

    def show_account_summary(self, acc_num: str):
        """Print account basic info and balance."""
        acc = self.get_account(acc_num)
        print(f"--- Account {acc_num} Summary ---")
        acc.info()
        print("------------------------------")

    def show_transactions(self, acc_num: str):
        """Print transaction history for a specific account."""
        acc = self.get_account(acc_num)
        acc.show_transactions()


# ---------------------------------------------
# Example interactive session (main program)
# ---------------------------------------------
def demo_run():
    """
    Demonstration of the system:
    - create accounts
    - deposit / withdraw
    - apply monthly interest
    - print summaries and transactions
    """
    print("=== Bank OOP Intermediate Demo (Monthly interest 5%) ===")
    bank = BankManager()

    # Create a savings account for Alice with initial deposit 1000
    acc1 = bank.create_savings("Alice", initial_deposit=1000.0, monthly_interest_rate=0.05)
    print(f"Created SavingsAccount {acc1} for Alice with initial deposit 1000")

    # Create a current account for Bob with initial deposit 500
    acc2 = bank.create_current("Bob", initial_deposit=500.0, minimum_balance=100.0, below_min_fee=10.0)
    print(f"Created CurrentAccount {acc2} for Bob with initial deposit 500")

    # Deposit and withdraw example
    bank.deposit_to(acc1, 200.0)  # deposit into Alice
    bank.withdraw_from(acc1, 50.0)  # withdraw from Alice

    bank.deposit_to(acc2, 100.0)  # deposit into Bob
    # Bob tries to withdraw an amount that will bring him below minimum
    success = bank.withdraw_from(acc2, 480.0)  # should fail or charge fee depending on policy
    print("Bob withdrawal success:", success)

    # Show balances before interest
    print("\nBalances BEFORE applying monthly interest:")
    bank.show_account_summary(acc1)
    bank.show_account_summary(acc2)

    # Apply monthly interest to all accounts (polymorphic behavior)
    print("\nApplying monthly interest to all accounts...")
    report = bank.apply_monthly_interest_all()
    for acc_num, interest in report.items():
        print(f"Account {acc_num} interest applied: {interest if interest else 0.0:.2f}")

    # Show balances after interest
    print("\nBalances AFTER applying monthly interest:")
    bank.show_account_summary(acc1)
    bank.show_account_summary(acc2)

    # Show transaction history for Alice
    print("\nAlice Transactions:")
    bank.show_transactions(acc1)

    # Show transaction history for Bob
    print("\nBob Transactions:")
    bank.show_transactions(acc2)

# Run demo if executed directly
if __name__ == "__main__":
    demo_run()
