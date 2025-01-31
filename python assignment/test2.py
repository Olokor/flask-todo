class  Create_account:
    def init (self ,name ,age ,phone_number , email,  BVN, pin ):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.BVN = BVN
        self.Pin = pin
        self.account_num = phone_number [1: ] if phone_number == 11 else phone_number[3:]

    def str (self):
        return  f"""(NAME: {self.name}, AGE: {self.age}, PHONE_NUMBER: {self.phone_number}, BVN: {self.BVN})"""

class Account_manager:
    accounts = []
    def create_accounts (self):
        entry = input("""
        Welcome to ME T U Banking system we are ready to give you the best  business transaction experience
        \n lets start by creating an account for you  \n input [Y] TO CREATE ACCOUNT OR [N] TO EXIT LOBBY  """).upper()
        while self.check_entry(entry):
                print("invalid input ")
                entry = input("""Valid response are ["Y","N"]""").upper()
        
        match entry:
            case "Y":
                Name = input ("enter full name : ")
                age = input("Enter your age : ")
                if self.check_age(age):
                    print("your cannot create an account")
                    return
                phone_no = input("Enter your phone_number : ")
                while True:
                    if self.check_phone_no(phone_no):
                        print("invalid phone number...")
                        phone_no = int(input("enter valid phone number"))
                    else:
                        break
                email = input("Enter your email : ") 
                BVN = int(input("enter BVN : "))
                Pin = int(input ("enter 4-digit pin"))
                print(f"CONGRATULATION {Name} you have created a METU Bank account ")
                self.accounts.append(Create_account(Name,Age,phone_no,email,BVN,Pin))
            case "N":
                return


    @staticmethod
    def check_entry(entry):
        if entry not in ["Y","N"]:
            return True
        return False

    @staticmethod
    def check_age(Age):
        
        try:
            Age = int(Age)
            if Age >= 105 or Age < 18:
                return True
            return False
        except ValueError:
            return True
        


    @staticmethod
    def check_phone_no(phone_no):
        try:
            phone_no = int(phone_no)
            return False
        except ValueError:
            return True
        


    @staticmethod
    def check_email(email):
        pass

    @staticmethod
    def check_bvn(BVN):
        pass
 
    @staticmethod
    def check_pin(pin):
        pass
        
            
create_accounts_ = Account_manager()
create_accounts_.create_accounts()