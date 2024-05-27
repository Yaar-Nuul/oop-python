class Account:
    def __init__(self, account_number, account_owner, balance):
        self.account_number = account_number
        self.account_owner = account_owner
        self.balance = balance
        self.transactions = []
        self.limit = 0
        self.minimum_balance = 0
        self.is_frozen = False
    
    def view_account_details(self):
        print("Account Details:")
        print("Account Number:", self.account_number)
        print("Account Owner:", self.account_owner)
        print("Current Balance:", self.balance)
    
    def change_account_owner(self, new_owner):
        self.account_owner = new_owner
        print("Account owner updated successfully.")
    
    def account_statement(self):
        print("Account Statement:")
        for transaction in self.transactions:
            print(transaction)
    
    def set_overdraft_limit(self, limit):
        self.overdraft_limit = limit
        print("Overdraft limit set successfully.")
    
    def interest_calculation(self, rate):
        interest = self.balance * rate
        self.balance += interest
        print("Interest applied successfully.")
    
    def freeze_account(self):
        self.is_frozen = True
        print("Account frozen.")
    
    def unfreeze_account(self):
        self.is_frozen = False
        print("Account unfrozen.")
    
    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
    
    def set_minimum_balance(self, min_balance):
        self.minimum_balance = min_balance
        print("Minimum balance set successfully.")
    
    def transfer_funds(self, recipient_account, amount):
        if self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            recipient_account.balance += amount
            print("Funds transferred successfully.")
            self.transactions.append(f"Transfer to {recipient_account.account_number}: ${amount}")
            recipient_account.transactions.append(f"Transfer from {self.account_number}: ${amount}")
        else:
            print("Insufficient funds to make the transfer.")
    
    def close_account(self):
        self.balance = 0
        self.transactions = []
        self.account_owner = "Closed Account"
        print("Account closed successfully.")

