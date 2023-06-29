class student: 
    def __init__(self,age,grades,name):
        self.age = age
        self.grades = grades
        self.name = name
    
    def myfunc(self):
        print("hi i am " + self.name + " and i am " + self.age + ",")
        print("i got " + self.grades + " overall") 

p1 = student("16","18/20","george" )
p1.myfunc()