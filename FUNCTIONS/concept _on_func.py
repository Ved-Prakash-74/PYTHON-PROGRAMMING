#A program to understand the basic concept on function

#sum of 2 number

from operator import mod


def sum(a,b):#called function....a,b are called formal parameters
    return a+b#returns value from called function to calling function
x=10
y=20
res=sum(x,y)#calling function.....x,y are called actual parameters
print(res)

#program to perform arithmetic operations
def arithmetic(x,y):
    return x+y,x-y,x*y,x/y,x%y
a=10
b=5
sum,sub,mul,div,mod=arithmetic(a,b)# or t=arithmetic(a,b)
print("\n")
print("addition =",sum)# print("addition =",t[0]
print("subtraction =",sub)#print("subtraction =",t[1]
print("multiplication =",mul)#print("multiplication =",t[2])
print("division =",div)#print("division =",t[3])
print("modulus =",mod)#print("modulus =",t[4])

#local variable
print("\n")
def fun():
    a=10
    print(a)
    fun1()
def fun1():
    b=20
    print(20)
fun()

#global variable
print("\n")
a=100
def fun2():
    a=10
    print(a)
    fun3()
    fun4()
    print(a)
def fun3():
    b=20
    print(b)
    print(a)
def fun4():
    global a
    a=a+1
    print(a)
fun2()

#types of function argument 
#i)Required or Positional argument
#ii)Keyword Argument
#iii)Default Argument 
#iv)Variable lenght or Arbitary Argument

# Required or Positional Argument 
print("\n")
def sub(a,b,c):
    print(a-b-c)
sub(10,20,30)
sub(20,30,10)
sub(30,20,10)

# Keyword Argument
print("\n")
def sub(a,b,c):
    print(a-b-c)
sub(a=10,b=20,c=30)
sub(c=30,a=10,b=20)
sub(b=20,a=10,c=30)

# Default Argument
print("\n")
def sum(a,b=20,c=30,d=40):#values must assigned from right to left
    print(a+b+c+d)
a=1
b=2
c=3
d=4
sum(1)
sum(1,2)
sum(2,3,4)
sum(1,2,3,4)

# Variable lenght or Arbitary Argument
print("\n")
def display(*n):
    print(n)
display()
display(10)
display(10,220)

def display(*n):
    s=0
    for i in n:
        s=s+i
    print(s)
display(10,20)





display(10,20,30)