class Georgenet:
    def __init__ (self):
        self.listofpeople = []
    def usernametaken(self, username):
        for person in self.listofpeople:
                if person.myname1 == username:
                    return True
        return False
        
   
   
    
class Person:
    def __init__ (self, myname1, myprd1):
        self.myname1 = myname1
        self.myprd1 = myprd1
        self.friendlist = []
        self.messages = []
    
