#Challenge Number:-4
# Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.


class Account:                                                          #parent class
    def __init__(self, title=0, Balance=0):                             #initializers for parent class
      self.title = title
      self.Balance = Balance
    
class SavingsAccount(Account):                                          #child class
    def __init__(self, title=0, Balance=0, intrestrate=0):              #initializers for child class
      super().__init__(title, Balance)                                  #initializers of child class created using initializers of parent class
      self.intrestrate = intrestrate

obj1 = Account("Ashish", 5000)
print(f"\nNAME OF ACCOUNT HOLDER IS: {obj1.title} : \nACCOUNT BALANCE IS: {obj1.Balance}")

obj2 = SavingsAccount("Ashish", 5000, 5)
print(f"\nNAME OF THE ACCOUNT HOLDER IS: {obj2.title}, \nACCOUNT BALANCE IS: {obj2.Balance},\nINTREST RATE IS: {obj2.intrestrate} ")
