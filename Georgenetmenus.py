def welcomemenu():
    print("")
    print("1. log in")
    print("2. creat an account")
    print("***************************************")
    number = input("please pick a number: ")
    return number


def loginmenu():
    print("")
    name = input("Name: ")
    password = input("Password: ")
    return name, password

def createaccountmenu():
    print("")
    myname1 = input("Name: ")
    myprd1 = input("Password: ")
    return myname1, myprd1

def main_menu():
    print("")
    print("1. edit details")
    print("2. friends list")
    print("3. block list")
    print("4. inbox")
    print("5. log out")
    print("6. quit")
    number1 = input("please pick a number: ") 
    return number1

def editdetailsmenu():
    print("")
    print("1. change name")
    print("2. change password")
    print("3. go back")
    number2 = input("please pick a number: ")
    return number2

def editname():
    name1 = input("please enter new name: " )
    return name1

def editpassword():
    prd1 = input("please enter new password: ")
    return prd1

def friendlist():
    friendusername = input("please enter name of person you want to add: ")
    return friendusername

def blobcklist():
     friendusername = input("please enter name of person you want to block: ")
     return friendusername

def message():
    messagesent = input("enter your message: ")
    return messagesent 

def personmsg():
    prsnmsg = input("enter name of person you want to send message to: ")
    return prsnmsg









