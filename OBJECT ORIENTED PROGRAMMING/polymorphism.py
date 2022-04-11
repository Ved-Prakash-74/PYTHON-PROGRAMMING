# polymorphism is derieved from greek word -> poly means many and morphism means forms
# it is represented in 3 ways:
#i)Operator Overloading
#ii) Method Overloading
#iii) Method Overriding

# Operator Overloading -> using same operator for different purposes. We can give extra meaning to existing 
# operator without changing its pervious meaning

class number:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __add__(self,other):
        a=self.a + other.a
        b=self.b + other.b
        c=self.c + other.c
        res=number(a,b,c)
        return res
    def __lt__(self,other):
        a=self.a + self.b + self.c
        b=other.a + other.b + other.c
        if(a < b):
            print(True)
        else:
            print(False)
n1=number(1,2,3)
n2=number(4,5,6)
n3=n1+n2 # or n3=number __add__(n1,n2)
print(n3.a,n3.b,n3.c)
print(n1 < n2)
#same way we can do subtraction, multiplication

#Method Overloading -> defining multiple methods with same name but with diffrent signature...Python doesn't
#support it, so we have use default argument given from right to left
print("\n")
class method_overloading:
    def display(self,a=None,b=None,c=None):
        print(a,b,c)
obj=method_overloading()
obj.display()
obj.display(10)
obj.display(10,20)
obj.display(10,20,30)

#Method Overriding -> implemented when inheritance is applied...for this we need to same name and same
# prototypes
print("\n")
class base:
    def display(self):
        print("Base Class")
class derieved(base):
    def display(self):
        print("Derieved Class")
ob=derieved()
ob.display() # -> the display() of derieved class over writes the defination of display() of its base class