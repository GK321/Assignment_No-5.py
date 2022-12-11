#Challenge Number:- 5


class Account(object):
    title=None
    balance=0
    # __init__ is known as the constructor
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
 
    def getbalance(self):
        return self.balance
        
    def deposit(self,amt):
        self.balance += amt
        # print(amt)
        
    def withdrawal(self, amt):
       self.amt = amt
       self.balance = self.balance - self.amt
    
# child class
 
 
class SavingsAccount(Account):
    interestrate=0
    def __init__(self, title, balance, interestrate):
        self.interestrate = interestrate
   
 
        # invoking the __init__ of the parent class
        Account.__init__(self, title, balance)
    def interestAmount(self):
        interest_amount=(self.interestrate*self.balance)/100 
        print("Interest is", interest_amount)
 
obj=Account("Ashish",2000)
# print(obj.getbalance())

obj.deposit(500)
print(obj.getbalance())

obj1=Account("Ashish",2000)
# print(obj1.getbalance())

obj1.withdrawal(500)
print(obj1.getbalance())

# creation of an object variable or an instance
obj1 = SavingsAccount('Ashish', 2000, 5)
 
# calling a function of the class Person using its instance
obj1.getbalance()
obj1.interestAmount()
obj1.withdrawal(500)
obj1.getbalance()
