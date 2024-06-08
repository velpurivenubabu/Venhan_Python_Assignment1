class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        self.balance += amount
    
    def withdraw(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
    
    def get_balance(self) -> float:
        return self.balance

# Example usage:
account = BankAccount("12585289", "venubabu", 2000.0)
print("Initial Balance:", account.get_balance())
account.deposit(800.0)
print("Balance after deposit:", account.get_balance())


withdrawal_result = account.withdraw(1500.0)
if withdrawal_result:
    print("Withdrawal successful. Balance after withdrawal:", account.get_balance())
else:
    print("Insufficient funds for withdrawal.")
