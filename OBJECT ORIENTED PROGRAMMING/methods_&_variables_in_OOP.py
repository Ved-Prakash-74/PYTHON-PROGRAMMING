#types of variables
#i) instance variable ->if the value of the object changes from one object to another then it is called 
# instance variable
#ii) static variable ->if the value of the variable is same for all the object then it is called static 
# variable
#iii) local variable ->the variables which are inside class or method are called local variables

#types of methods
#i) instance method -> it is used to access instance variable as well as static variable and are accesses by
# object.
#ii) static method -> used to access static variables
#iii) classmethod -> used to access class level methods

class student:
    univ="xyz" #static variable
    def __init__(self,rno,name): #rno, name is local variable
        self.rno=rno #instance variable
        self.name=name #instance variable
    def display(self): #instance method
        print(self.rno,self.name)
        print(student.univ) #access static variable
    @ staticmethod #static method
    def show():
        student.univ="abc"
        print(student.univ)
    @ classmethod #class method
    def cmethod(cls):
        cls.univ="pqrs"
        print(cls.univ)
s1=student(72,"max")
s1.display()
s2=student(73,"steve")
s2.display()
student.show()
student.cmethod()