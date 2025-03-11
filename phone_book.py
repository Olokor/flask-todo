phone_book = {}

def addContactDetail(firstname:str, lastName:str, number:str):
    phone_book[firstname] = [firstname, lastName, number]

def deleteContactDetail(firstname:str):
    phone_book.pop(firstname)

def editContactDetail(firstname:str):
    details = phone_book[firstname]
    print("what do you want to change....")
    newdetail = input("enter firstname, lastname or phonenumber")
    match newdetail:
        case firstname:
            updateDetail(firstname:str)

def updateFirstName(firstname:str, detail:str):
    details = phone_book[firstname]
    details[0] = details

def 