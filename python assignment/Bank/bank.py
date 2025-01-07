class Account:
    def __init__(self, account_name:str, email:str, address:str, phone_number:str, bvn:str, pin:str, deposit_amount = 0.00,):
        self.account_name = account_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.bvn = bvn
        self.pin = pin
        self.account_balance = deposit_amount
        self.account_number = phone_number[1:] if (len(phone_number)==11) else phone_number[3:]

    def __str__(self):
        return f"""
    (account name: {self.account_name}, address:{self.address}, phone number:{self.phone_number}
    email:{self.email}, bvn:{self.bvn}, account balance: {self.account_balance}, account number:{self.account_number})"""



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
        while True:
            if self._check_phone_number(phone_number):
                break
            print("invalid phone number..")
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
        

    def _login(self, accounts:Account):
        print("your login details are you account number and pin...")
        user_id = input("enter your account number>>>> ")
        pin = input("enter your pin")
        for account in accounts:
            if (account.account_number == user_id) and (account.pin == pin):
                return account
            
        return None

    def _getUserDetails(self, account_number):
        for account_details in self.accounts:
            if account_details.account_number == account_number:
                return account_details
    

    def _transfer_money(self,amount:float, account_number:str):
        recipient_account = self._getUserDetails(account_number)
        if recipient_account:
            recipient_account.account_balance += amount
    
    def _withdraw_money(self, amount, account:Account):
        account.account_balance -= amount
    
    def _get_account_balance(self, account:Account):
        return account.account_balance
    
    def _recharge_personal_line(self,amount:float, account:Account):
        if amount >= 50 and account.account_balance > amount:
            account.account_balance -= amount
    
    def _recharge_a_friend(self, amount:float, phone_number:str, account:Account):
        if amount >= 50 and account.account_balance > amount and self._check_phone_number(phone_number):
            account.account_balance -= amount
    
    def bank_interface(self):
        print("""
        Welcome to the USSD interface.
        1. Create account
        2. Login
        >>>>>> """)
        loggedInUser = None
        entry = input()
        match (entry):
            case "1":
                while True:
                    self._create_account()
                    response = input("do you want to create another account y/n?>>> ").lower()
                    if response in ["no", "n"]:
                        break
                loggedInUser = self._login(self.accounts)
            case "2": loggedInUser = self._login(self.accounts)

            case _:
                print("ivalid input, please enter a valid input")
            
        
        
        while True:
            print("""
            Welcome to the USSD interface.
            1. Check account balance
            2. Withdraw money
            3. transfer money
            4. Recharge line (personal)
            5. Recharge line (external)
            6. Exit
            >>>>>> """)

            entry = input()
            match entry:
                case "1":
                    balance = self._get_account_balance(loggedInUser)
                    print(f"your account balance is N{balance}")
                
                case "2":
                    try:
                        amount = float(input("enter amount you want to withdraw>>>> "))
                        if loggedInUser.account_balance > amount and amount > 500:
                            loggedInUser.account_balance -= amount
                            print("transction successful...")
                            print(f"your current balance is {loggedInUser.account_balance}")
                        else:
                            print("insufficient balance... ")
                    except ValueError:
                        print("invalid amount")
                
                case "3":
                    try:
                        amount = float(input("enter amount you want to withdraw>>>> "))
                        account_number = input("enter account number>>>> ")
                        if loggedInUser.account_balance > amount and amount > 500:
                            if self._transfer_money(amount, account_number) is not None:
                                print("transction successful...")
                                print(f"your current balance is {loggedInUser.account_balance}")
                            else:
                                print("account not found")
                        else:
                            print("insufficient balance... ")
                    except ValueError:
                        print("invalid amount")
                
                case "4": 
                    try:
                        amount = float(input("enter amount you want to recharge>>> "))
                        if loggedInUser.account_balance > amount and amount > 50:
                            self._recharge_personal_line(amount, loggedInUser)
                            print("your airtime is on it way......")
                        else:
                            print("insufficient funds or amount lower than 50 naira...")
                    except ValueError:
                        print("invalid input")
                
                case "5":
                    try:
                        amount = float(input("enter amount you want to recharge>>> "))
                        phone_number = input("enter phone number")
                        if loggedInUser.account_balance > amount and amount > 50 and self._check_phone_number(phone_number):
                            self._recharge_a_friend(amount, phone_number, loggedInUser)
                            print("your airtime is on it way......")
                        else:
                            print("insufficient funds or amount lower than 50 naira or invalid phone number...")
                    except ValueError:
                        print("invalid input")
                
                case "6":
                    break

                case _:
                    print("invalid input")
                    break
                





    @staticmethod
    def _check_phone_number(phone_number:str):
        if "+234" in phone_number:
            try:
                number = int(phone_number[3:])
                return True
            except ValueError:
                return False
        else:
            try:
                number = int(phone_number)
                return True
            except ValueError:
                return False
        

    
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
    



new_account_manager = AccountManager()
new_account_manager.bank_interface()