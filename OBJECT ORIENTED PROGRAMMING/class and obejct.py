# class :- it is a blue print or plan from which an object is created
# object :- it is an instance of a class

class student:
    roll=10
    name="Zeo"
    def display(self):
        print("Roll is:",self.roll)
        print("Name is:",self.name)
s1=student()
s1.display()
s2=student()
s2.roll=20
s2.name="Ozuma"
s2.display()