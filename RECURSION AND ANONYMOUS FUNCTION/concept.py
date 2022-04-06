#concept on recursion
#calling function and called function must be same....a base condition must be given to terminate

# factorial of given number using recursion
def fac(n):
    if(n==0):
        return 1
    else:
        return n*fac(n-1)
print(fac(5))

#concept on anonymous function
# it is a function without name
#example : 1....square of a number
s=lambda n:n*n
print(s(4))

#example : 2....addition of two numbers
s=lambda x,y:x+y
print(s(1,2))
print(s(10,20))