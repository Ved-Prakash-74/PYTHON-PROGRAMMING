#raise keywod is used to throw an raised exception into except block
#Exception is the base class for all build in exception

#example 1
from logging import exception


a=10
b=0
try:
    if(b==0):
        raise ZeroDivisionError
except ZeroDivisionError:
    print("\nDivided by Zero")

#example 2
marks=int(input("\nEnter marks: "))
try:
    if(marks < 0 or marks > 100):
        raise exception
    print(marks)
except:
    print("\nMarks should be between 0 and 100")