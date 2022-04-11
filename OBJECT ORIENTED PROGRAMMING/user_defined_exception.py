#it is also called custom exception
#let us consider the example of voting...if age is above 18 then they are allowed to vote else not

class voting(Exception):
    pass
age=int(input("\nEnter age: "))
try:
    if(age < 0 or age <18):
        raise voting
    print("\nEligible for voting")
except voting:
    print("\nAge should greater than 18")