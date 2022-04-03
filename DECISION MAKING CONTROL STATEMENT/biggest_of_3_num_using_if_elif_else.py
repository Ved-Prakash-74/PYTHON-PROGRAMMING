#python program to print biggest og 3 numbers using if-elif-else

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a>b and a>c):
    print(a,"is biggest")
elif(b>a and b>c):
    print(b,"is biggest")
else:
    print(c,"is biggest")