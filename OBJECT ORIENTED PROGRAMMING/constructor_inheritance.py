# parameters are passed to base class constructors from derieved class which is done using 'super keyword'
#if derieved class has constructor then base class constructor won't get executed , so it order to do that we
# have to super() keyword 

class base:
    def __init__(self,rno,name):
        print("Super class constructor")
        self.rno=rno
        self.name=name
class derieved(base):
    def __init__(self,rno,name,age):#if derieved class has constructor then base class constructor - 
        self.rno=rno                # - won't get executed
        self.name=name
        self.age=age
        print("Sub class constructor")
    def display(self):
        print(self.rno,self.name,self.age)
d=derieved(72,"max",25)
d.display()
d=derieved(72,"max",35)
d.display()

#using super keyword to access base class
print("\n")
class base:
    def __init__(self,rno,name):
        print("Super class constructor")
        self.rno=rno
        self.name=name
class derieved(base):
    def __init__(self,rno,name,age):
        super().__init__(rno,name)
        self.age=age
        print("Sub class constructor")
    def display(self):
        print(self.rno,self.name,self.age)
d=derieved(72,"max",25)
d.display()
d=derieved(72,"max",35)
d.display()