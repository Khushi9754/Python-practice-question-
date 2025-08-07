class Atm:
    #constructor , __init__
    def __init__(self):
        #instance var
        self.pin=""
        self.balance=0
        
        self.menu()
        
    def menu(self):
        while True:
            user_input=int(input("""
                                Hello!, choose to proceed:
                                1.Enter 1 to create pin
                                2.Enter 2 to deposit
                                3.Enter 3 to withdraw
                                4.Enter 4 to check balance
                                5.Enter 5 to exit
                                Enter choice:
                                """))
            
            if user_input==1:
                self.create_pin()
            elif user_input==2:
                self.deposit()
            elif user_input==3:
                self.withdraw()
            elif user_input==4:
                self.check_balance()
            elif user_input==5:
                self.bye()
            else:
                print("Invalid input,Please enter your choice again")
            
    def create_pin(self):
        self.pin=(input("enter pin:"))
        print("Pin created Successfully")
        
    def deposit(self):
        check=(input("enter the pin:"))
        if check==self.pin:
            temp=int(input("enter the amount:"))
            self.balance=self.balance+temp
            print("Money deposited")
        else:
            print("Invalid pin")
            
    def withdraw(self):
        check=(input("enter the pin:"))
        if check==self.pin:
            temp=int(input("enter the amount:"))
            if self.balance>=temp:
                self.balance=self.balance-temp
                print("Withdraw is done")
        else:
            print("Invalid pin")
                
    def check_balance(self):
        check=(input("enter the pin:"))
        if check==self.pin:
            print("Balance:",self.balance)
        else:
            print("Invalid Pin")
            
    def bye(self):
        print("Thank you!")
        exit()
        
#obj -> Reference variable        
obj=Atm()