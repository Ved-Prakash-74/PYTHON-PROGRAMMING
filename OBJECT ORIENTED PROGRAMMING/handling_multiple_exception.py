# atry block can multiple except block

try:
    a=10
    b=2
    l=[10,20,30]
    print(a/b)
    print(l[10])
except ZeroDivisionError:
    print("\nDivision by Zero")
except IndexError:
    print("\nIndex out of range")
except: #default exception block which handles all exception
    print("\nException occured")
    