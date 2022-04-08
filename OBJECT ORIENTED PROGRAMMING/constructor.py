#cnstructor :- it is an special method used to initialize an object
# types :- i) parameterless constructor ii) parameterised constructor

#example of parameterless constructor
class student:
    def __init__(self):
        self.roll=10
        self.name="tylor"
    def display(self):
        print("roll is:",self.roll)
        print("name is:",self.name)
s1=student()
s1.display()
s2=student()
s2.roll=20
s2.name="brine"
s2.display()

#example of parameterised constructor
print("\n")
class student:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def display(self):
        print("roll is:",self.roll)
        print("name is:",self.name)
s1=student(10,"daisy")
s1.display()
s2=student(20,"chris")
print("roll is:",s2.roll,"\nname is:",s2.name)