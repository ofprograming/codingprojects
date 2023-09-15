#yairvinsh 

class ravKav: 
    
    def __init__(self, age, balance = 0): 
        self.age = age
        self.balance = balance 
        self.maxBalance = 300
    
    def charge(self, M2C): 
        if self.age >= 18: 
            bonus = M2C * 0.1
        else: 
            bonus= M2C *0.5 
            
        total_money = M2C + bonus 
        
        if self.balance + total_money > self.maxBalance: 
            print("charge exceeds max balance of 300, current balance: {self.balance}")
        else: 
            self.balance += total_money
            print(f"successfully charged {M2C}, the bonus added is {bonus}, total amount : {self.balance} ")
            
user_age = int(input("enter age:"))
user_money = int(input("enter the wished sum to charge:"))

existing_balance = float(input("enter the existing balance"))
user_card = ravKav(user_age, existing_balance)

user_card.charge(user_money)