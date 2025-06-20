class BankAccount:
    bank_title = "CS Bank"
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number
    def deposit(self, amount):

        if amount > 0:
            self.current_balance += amount
            print(f"Depositing ${amount} to {self.customer_name}'s account.")
        else:
            print("Deposit amount must be positive.")
        self.current_balance += amount
        
    def withdraw(self, amount):
        remaining_balance = self.current_balance - amount
        if remaining_balance < self.minimum_balance:
            print("CANNOT WITHDRAW INSUFFICIENT BALANCE\n")
        else:
            self.current_balance = remaining_balance

            print(f"Withdrew ${amount} from {self.customer_name}'s account.")

    def print_customer_information(self):
        print(f"Customer Bank: {self.bank_title}\nCustomer Name: {self.customer_name}\nCurrent Balance: {self.current_balance}\nMinimum Balance: {self.minimum_balance}\n")


