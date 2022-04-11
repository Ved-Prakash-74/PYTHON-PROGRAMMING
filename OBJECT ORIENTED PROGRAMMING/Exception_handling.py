#Exception handling types -> i)Syntax or compile time error ii) Logical error iii) Exception
#Exception -> it is arun time error which occur during program execution and program will get abnormally 
# terminated

#Handling exception
# i) try -> a list of statements that generates exception
# ii) except -> a list of statements that handles exception
# iii) else -> a list of statements which gets exceuted when there is no exception
# iv) finaly -> always gets exceuted

a=int(input("\nEnter 1st number: "))
b=int(input("\nEnter 2nd number: "))
try:
    c=a/b
    print(c)
except:
    print("\nException occured")
else:
    print("\nAll's ok")
finally:
    print("\nEnd")   