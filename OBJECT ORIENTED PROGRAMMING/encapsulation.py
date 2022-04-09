#encasulation means wrapping up of variables and functions in a single unit
# major advantage of it is 'data hiding' which means we can declare any variable as private or public

#example when no variable are in public mode
class encap:
    a=10
    def display(self):
        print(self.a)
e=encap()
e.display()

#example when variable are in private mode
print("\n")
class encap:
    __a=10 #private variable denoted by 2 underscore symbol
    def display(self):
        print(self.__a) # the way of accessing private variable
e=encap()
e.display()

#to acces private members variables we can use i) setter -> used to set values ii) getter -> used to get values
print("\n")
class encap:
    __a=10
    def setA(self,b):
        self.__a=self.__a+b
    def getA(self):
        return self.__a
e=encap()
e.setA(30)
print(e.getA())
