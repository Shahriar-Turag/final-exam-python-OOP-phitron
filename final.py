class Bank:
    total_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        Bank.total_balance += amount
        self.transaction_history.append(f"Deposit: +${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            Bank.total_balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
        else:
            print("Insufficient funds. Unable to withdraw.")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            recipient.deposit(amount)
            self.balance -= amount
            Bank.total_balance -= amount
            self.transaction_history.append(f"Transfer to {recipient.account_holder}: -${amount}")
        else:
            print("Insufficient funds. Unable to transfer.")

    def check_balance(self):
        return f"Available Balance: ${self.balance}"

    def request_loan(self, loan_amount):
        if Bank.loan_feature_enabled:
            total_amount = self.balance + Bank.total_loan_amount
            if loan_amount <= total_amount * 2:
                Bank.total_loan_amount += loan_amount
                self.balance += loan_amount
                self.transaction_history.append(f"Loan: +${loan_amount}")
                print(f"Loan of ${loan_amount} approved.")
            else:
                print("Loan amount exceeds limit.")
        else:
            print("Loan feature is currently disabled.")

class Admin:
    @staticmethod
    def enable_loan_feature():
        Bank.loan_feature_enabled = True
        print("Loan feature is now enabled.")

    @staticmethod
    def disable_loan_feature():
        Bank.loan_feature_enabled = False
        print("Loan feature is now disabled.")

    @staticmethod
    def check_total_balance():
        return f"Total Bank Balance: ${Bank.total_balance}"

    @staticmethod
    def check_total_loan_amount():
        return f"Total Loan Amount: ${Bank.total_loan_amount}"


user1 = Bank("User1", 1000)
user2 = Bank("User2", 1500)
admin = Admin()

user1.deposit(500)
user1.withdraw(200)
user1.transfer(user2, 300)
print(user1.check_balance())
user1.request_loan(1000)

print(admin.check_total_balance())
print(admin.check_total_loan_amount())
admin.disable_loan_feature()
user1.request_loan(500)