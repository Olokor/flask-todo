class Account:
    def __init__(self, account_name:str, email:str, address:str, phone_number:str, bvn:str, pin:str, deposit_amount = 0.00,):
        self.account_name = account_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.bvn = bvn
        self.pin = pin
        self.accoun_balance = deposit_amount
        self.account_number = phone_number[1:] if (len(phone_number)==11) else phone_number[3:]

        def __str__(self):
            return f"""
        (account name: {account_name}, address:{address}, phone number:{phone_number}
        email:{email}, bvn:{bvn}, account balance: {self.account_balance}, account number:{self.account_number})"""

class AccountManager:
    accounts = []

    def _create_account(self):
        print("""
        welcome to our mobile banking service, we are dedicated to offering you the bests 
        service and manage your money with our heart
        lets get you started by creating an account for you
        please fill the form below with correct details""")

        account_name = input("enter your full name>>>> ")
        address = input("Enter your residential address")
        email = input("enter email adress>>>> ")
        while True:
            if self._check_email(email):
                print("please enter a valid email...")
                email = input("enter email adress>>>> ")
            else:
                break
        
        phone_number = input("Enter your mobile number>>> ")
        bvn = input("Enter your BVN>>>>>> ")
        pin = input ("Enter your pin(4 digit number)")
        while True:
            if self._check_pin(pin):
                print("pin must be 4 digits only...")
                pin = input ("Enter your pin(4 digit number)")
            else:
                break
        
        # check if user wants a zero account or wants to deposit money
        response = input("do you want to deposit money in your account y/n? ").lower()
        if response in ["y", "yes"]:
            amount = float(input("enter amount"))
            self.accounts.append(Account(account_name,email,address,phone_number,bvn,pin,amount))
        elif response in ["n", "no"]:
            self.accounts.append(Account(account_name,email,address,phone_number,bvn,pin))
        

    def _login(self, accounts:list):
        print("your login details are you account number and pin...")
        user_id = input("enter your account number>>>> ")
        pin = input("enter your pin")
        for account in accounts:
            if (user_id in account) and (pin in account):
                return account
            
        return None


    def _transfer_money(amount:float, account_number:str, accoount:list):
        ...
        
    
    @staticmethod
    def _check_email(email):
        mail_domin = ["gamil", "yahoo", "hotmail", ".com"]
        if "@" in email:
            for domin in mail_domin:
                if domin in email:
                    return False
                
        return True
    
    @staticmethod
    def _check_pin(pin):
        if len(pin) == 4:
            try:
                int_pin = int(pin)
                return False
            except ValueError:
                return True
    

