class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
            self.balance -= amount

    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance: ₹", self.balance)


a = int(input("Enter account number: "))
n = input("Enter name: ")
t = input("Enter account type: ")
b = float(input("Enter balance: "))

acc = BankAccount(a, n, t, b)
acc.display()

d = float(input("\nEnter amount to deposit: "))
acc.deposit(d)

w = float(input("Enter amount to withdraw: "))
acc.withdraw(w)

acc.display()
