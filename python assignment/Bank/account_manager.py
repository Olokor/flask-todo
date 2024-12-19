class Create_Account:
    def __init__(self, account_name:str, phone_number:str, home_address:str, BVN:str, deposit_amount=None, ):
        self.account_name = account_name
        self.phone_number = phone_number
        self.home_address = home_address
        self.BVN = BVN
        self.deposit_amount = deposit_amount
        self.account_balance = deposit_amount
        self.account_number = phone_number[1:] if len(phone_number == 11) else phone_number[3:]
    
    def account_details(self)->str:
        print(f"Welcome to Dev_0 bank of africa (DBA plc)/n your account
              Account Details/n
              account name: {self.account_name}/n
              account number: {self.account_number}/n
              account blance: {self.account_balance}/n
              BVN: {self.BVN}") 
        


class AccountManager(Create_Account):
    def __init__(self, account_name, phone_number, home_address, BVN, deposit_amount=None):
        super().__init__(account_name, phone_number, home_address, BVN, deposit_amount)
    
    @staticmethod
    def check_correct_parameter(amount:float):
        if (type(amount) not in [int, float]) or (amount <= 0):
            return False
        return True
    def deposit_money(self, amount:float):
        if (self.check_correct_parameter(amount)):
            self.account_balance += amount
        raise TypeError
    
    def withdraw_money(self, amount:float):
        if (self.check_correct_parameter(amount)):
            if (self.account_balance > amount):
                self.account_balance -= amount
        raise TypeError
    
    def transfer_money(self, amount:float, account_number:str, all_account:list):
        if (self.check_correct_parameter(amount)):
            for account_id in all_account:
                if (account_number in account_id) and (self.account_balance > amount):
                    self.account_balance -= amount




