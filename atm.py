class atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin 

    def check_balance(self):
        print("Your balance is 50,000")

    def withdrawl(self, amount):
        if(amount>50000):
            new_balance = amount - 50000
            print("Your loan is ==>"+str(new_balance)) 
        elif(amount<=50000):
            new_balance = 50000 - amount
            print("Your amount left is ==>"+str(new_balance))
    



def main():
    card_number = input("enter your card number ==> ")
    pin_number = input("enter your pin number ==> ")
    
    new_user = atm(card_number, pin_number)
    print("Choose your activity ")
    print("1. Balance Enquiry   2. Withdrawl")

    
    activity = int(input("Enter Activity Number ==>"))

    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("Amount to be withdrawn ==>"))
        new_user.withdrawl(amount)
    else:
        print("select a valid activity")
    
main()