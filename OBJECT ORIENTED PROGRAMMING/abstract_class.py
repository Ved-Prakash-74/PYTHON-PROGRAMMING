#Abstract Class
#abstract class is the collection of abstract method. It should not instanciated(process of creating a object)
#It is implemented when inheritance is done 

#Abstract Method
#it has declaration part but no defination part is there

from abc import ABC,abstractmethod
class abstract_demo1(ABC):
    @abstractmethod
    def display(self):
        pass
class abstract_demo2(abstract_demo1):
    def display(self):
        print("Abstract demo 2")
ob=abstract_demo2()
ob.display()

# the class will provide the defination of abstract class
# we can't create object for abstract class
 