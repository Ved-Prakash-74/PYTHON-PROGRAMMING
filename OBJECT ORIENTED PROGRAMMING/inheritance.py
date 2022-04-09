#inheritance means the process of creating a new class from a class which is already existing
#advatnge -> reusability
#types -> i) single inheritance ii) multiple inheritance iii) hierarchical inheritance iv) multi level
#  inheritance

#single inheritance -> it will have single base class and single derieved class 
class base:
    def fun1(self):
        print("function 1")
class derieved(base):
    def fun2(self):
        print("function 2")
d=derieved()
d.fun1()
d.fun2()

#multiple inheritance -> it will have multiple base classes and one derieved class
print("\n")
class base1:
    def fun1(self):
        print("function 1")
class base2:
    def fun2(self):
        print("function 2")
class derieved(base1,base2):
    def fun3(self):
        print("function 3")
d=derieved()
d.fun1()
d.fun2()
d.fun3()

#hierarchical inheritance -> it will have one base class and multiple derieved class
print("\n")
class base:
    def fun1(self):
        print("function 1")
class derieved1(base):
    def fun2(self):
        print("function 2")
class derieved2(base):
    def fun3(self):
        print("function 3")
d1=derieved1()
d2=derieved2()
d1.fun1()
d1.fun2()
d2.fun1()
d2.fun3()

#multi-level inheritance -> the inheritance will be level by level
print("\n")
class A:
    def fun1(self):
        print("function 1")
class B(A):
    def fun2(self):
        print("function 2")
class C(B):
    def fun3(self):
        print("function 3")
ob=C()
ob.fun1()
ob.fun2()
ob.fun3()