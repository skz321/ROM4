from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer_amount(self, transfer_amount, recipient_name):
        if (transfer_amount > self.transfer_limit):
            print("The transfer amount exceeds the transfer limit")
        elif (self.minimum_balance > self.current_balance - transfer_amount):
            print("The transfer amount exceeds the minimum balance")
        else:
            self.current_balance -= transfer_amount
            print(f"{self.customer_name} transferred ${transfer_amount} to {recipient_name}")
            print(f"Current balance is now: ${self.current_balance}")

