from Georgenetmenus import *
from Georgenetclasses import Georgenet, Person

Georgenet = Georgenet()

def mainloop(pers):
    mainmenu = main_menu()
    while True:
        if mainmenu == "1":
            print("")
            print("your name is: " + pers.myname1)
            print("your password is: " + pers.myprd1) 
            edit = editdetailsmenu()
            while True:
                if edit == "1":
                    editname1 = editname()
                    pers.myname1 = editname1
                if edit == "2":
                    editprd1 = editpassword()
                    pers.myprd1 = editprd1
                if edit == "3": 
                    break
                print("")
                print("your name is: " + pers.myname1)
                print("your password is: " + pers.myprd1) 
                edit = editdetailsmenu()
        if mainmenu == "2":
            if len(pers.friendlist) == 0:
                print("you have no friends")
            elif len(pers.friendlist) >= 1:
                for person in pers.friendlist:
                    print(person)
            print("")
            print("Add friends:")
            print("")
            for person in Georgenet.listofpeople:
                if person.myname1 != pers.myname1 :
                    print(person.myname1)
            print("")
            friendusername = friendlist()
            if Georgenet.usernametaken(friendusername):
                    pers.friendlist.append(friendusername)
            else:
                print("")
                print("person not found")


        if mainmenu == "3":
            if len(pers.friendlist) == 0:
                print("you have no friends")
            elif len(pers.friendlist) >= 1:
                for person in pers.friendlist:
                    print(person)
            print("")
            print("block friends: ")
            print("")
            friendusername = friendlist()
            if Georgenet.usernametaken(friendusername):
                pers.friendlist.remove(friendusername)
            else:
                print("")
                print("person not found")
        if mainmenu == "4":
            print("")
            if len(pers.messages) == 0:
                print("you have no messages")
            elif len(pers.messages) >= 1:
                for person in pers.messages:
                    print(person)
            print("")
            print("send a message: ")
            print("")
            if len(pers.friendlist) == 0:
                print("you have no friends")
                mainmenu = main_menu()
                continue
            elif len(pers.friendlist) >= 1:
                for person in pers.friendlist:
                    print(person)
            friendusername = personmsg()
            if Georgenet.usernametaken(friendusername):
                    print("")
                    msg = message()
                    for person in Georgenet.listofpeople:
                        if friendusername == person.myname1:
                            person.messages.append(pers.myname1 + ":" + msg )
                
            else:
                print("")
                print("person not found")
            
            
        if mainmenu == "5":
            return None

        if mainmenu == "6":
            exit()
        mainmenu = main_menu()


if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Georgenet")
    print("########################################################")
    choice = welcomemenu()

    while True:
        if choice == "1":
            myname1, myprd1 = loginmenu()
            for person in Georgenet.listofpeople:
                if myname1 ==  person.myname1:
                    if myprd1 == person.myprd1:
                        print("")
                        print("welcome back " + myname1)
                        mainloop(person)

            
        if choice == "2":
            myname1, myprd1 = createaccountmenu()
            pers = Person(myname1, myprd1)
            Georgenet.listofpeople.append(pers)
            mainloop(pers)
        choice = welcomemenu()