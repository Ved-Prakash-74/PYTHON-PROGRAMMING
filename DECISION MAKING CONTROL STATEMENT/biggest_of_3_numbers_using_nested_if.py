#python program to print biggest of 3 numbers using nested if

a=int(input("Enter 1st number:"))
b=int(input("Enter 1st number:"))
c=int(input("Enter 1st number:"))
if(a>b):
    if(a>c):
        print(a,"is largest")
    else:
        print(c,"is largest")
else:
    if(b>c):
        print(b,"is largest")
    else:
        print(c,"is largest")
