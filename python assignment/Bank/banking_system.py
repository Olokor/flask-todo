class Create_account:
    """class to create account
    """

    def __init__(self):
        self.create_new_account()


    def create_new_account(self):
        print(""""
            welcome to Dev_0 online banking(DOB plc)...
            we are dedicated to deliverying the best banking experience for our user
            your money management and satisfaction is our altmost priority..
            let's get you started by creating an account for you now.
            Enjoy the GOOD LIFE...""")
        self.account_name = input("Enter your full name>>>> ")
        self.phone_number = input("Enter your phone number>>> ")
        self.address = input("Enter your current address>>> ")
        self.account_balance = 0.00
        print("will you like to deposit some money in your newly created account or you want to create a zero account?")
        response = input("enter Y/N").lower()
        if response == "y":
            deposit_amount = float(input("enter deposit amount>>>> "))
            self.account_balance = deposit_amount
        
        self.account_number = self.phone_number[1:] if (len(self.phone_number) == 11) else self.phone_number[3:]
        self.BVN = input("enter your BVN>>>> ")
        self.account_password = input("enter your account password")



class AccountManager:
    account_database = {}
    id = 0

    # create user session
    def login_account(self):
        if self.account_database is not None:
            print("your login details are your account number and password....")
            account_number = input("enter account number>>>> ")
            password = input("enter password>>>> ")

            for id, account_details in self.account_database.items():
                if "9112113242" in account_details.values() and "12345" in account_details.values():
                    print(f"welcome {account_details['account name']}")
                    return True, account_details
        print("invalid credentials")
        return False, None
        


    def create_account(self):
        while True:
            new_account = Create_account()
            self.id += 1
            self.account_database[self.id] = {
                "account name": new_account.account_name,
                "adress": new_account.address,
                "phone number": new_account.phone_number,
                "account number": new_account.account_number,
                "account balance": new_account.account_balance,
                "BVN": new_account.BVN,
                "password": new_account.account_password
            }
            response = input("do you want to create another account? y/n").lower()
            if (response in ["y", "yes"]):
                print("okay, enter new details")
            elif(response in ["n", "no"]):
                break
            else:
                raise TypeError
    
    def print_accounts(self):
        for account, account_details in self.account_database.items():
            print(f"{account} : {account_details}")

    
    def transfer_money(self, amount:float, account_number:str): 
        print(f"hello customer\n please login your account")
        session = self.login_account()
        if session and session[0]:
            if  session[1]["account balance"] > amount:
                for id, account_details in self.account_database.items():
                    if account_number in account_details.values():
                        account_details["account balance"] += amount
                        session[1]["account balance"] -= amount
                        print("transction completed!!")
                    else:
                        print("recipient account not found")
                        return
            else:
                print("Insufficient funds!")
                return
        print("you are not logged in...")
    
    def withdraw_money(self, amount):
        ...

    def ussd(self):
        print("""
        welcome to 737 service...
        1. to deposit money 
        2. to recharge your line
        3. to recharge external line
        4. to transfer money
        5. to withdraw money
        6. to pay bills""")

        get_input = input(">>>>>>>>> ")
        match get_input:
            case "1":
                print("we are working on this section \n please pick another option")

            case "2":
                print("your airtime is on it way, thanks for choosing our service..") 
            
            case "3":
                print("airtime to your loved one is on it was \n thanks for choosing our service..")
            
            case "4":
                amount = float(input("enter amount>>> "))
                account_number = input("enter account number>>> ")
                self.transfer_money(amount, account_number)
            
            case "5":
                print("this featuer is still under developnment...")

            case "6":
                print("this feature is still under development")

            case _:
                session = self.login_account()
                if session and session[0]:
                    print(session[1])
            
            


        

    
first_account = AccountManager()
first_account.create_account()

    


