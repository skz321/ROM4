from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# Scenario:  Wes opens a checking account
print("Wes Checking Account")
WesCheckingAccount = CheckingAccount("Wes", 1520,100, "213213", "4320213", 100)
# Wes Withdraws too much money
WesCheckingAccount.withdraw(1500)
# Wes Withdraws a good amount of money
WesCheckingAccount.withdraw(200)
WesCheckingAccount.print_customer_information()
# Wes Tries to transfer too much money to Jack's checking account
WesCheckingAccount.transfer_amount(200, "Jack")
# Wes transfers money to Jack's checking account
WesCheckingAccount.transfer_amount(100, "Jack")
WesCheckingAccount.print_customer_information()

# Scenario: Jack opens a checking account
print("Jack Checking Account")
JackCheckingAccount = CheckingAccount("Jack", 2000,300, "2323213", "6774223", 50)

# Jack Withdraws a good amount of money
JackCheckingAccount.withdraw(200)
JackCheckingAccount.print_customer_information()
# Jack Tries to transfer too much money to Jack's checking account
JackCheckingAccount.transfer_amount(200, "Wes")
# Jack transfers money to Jack's checking account
JackCheckingAccount.transfer_amount(50, "Wes")
JackCheckingAccount.print_customer_information()

# Wes opens savings account
WesSavingsAccount = SavingsAccount("Wes", 2000, 100, "213213", "4320213", .05)

# Wes applys interest to account
WesSavingsAccount.apply_interest()
# Jack opens saving account
JackSavingsAccount = SavingsAccount("Jack", 2000, 300, "2323213", "6774223", .03)
# Jack applys interst to account
JackSavingsAccount.apply_interest()