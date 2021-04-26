class Customer:
    def __init__(self,firstName, lastName, social):
        self.firstName = firstName 
        self.lastName = lastName 
        self.social = social 

    def setfirstName(self,firstName):
        self.firstName = firstName

    def setlastName(self,lastName):
        self.lastName = lastName

    def __str__(self):
        self.name = "{},{} (SSN:{})".format(self.firstName, self.lastName,self.social)
        return self.name 
class BankAccount(Customer):
    from random import randint
    n = 10
    range_start = 10**(n-1)
    range_end = (10**n)-1
    accountNumber = randint(range_start, range_end)

    def __init__(self,customer,balance = 0):
        self.customer = customer
        self.balance = balance 

    def setCustomer(self,customer,accountNumber):
        self.customer = customer
        self.accountNumber = accountNumber 

    def getCustomer(self,customer,accountNumber):
        return self.customer, self.accountNumber

     def __str__(self):
        customer = "{} account number: {}, balance: ${}".format(self.customer,self.accountNumber,self.balance)
        return customer
