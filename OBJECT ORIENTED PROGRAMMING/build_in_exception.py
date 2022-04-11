# there are 10 build in exception

#i) Attribute Error -> raised when object is trying to access an attribute whuch doesn't exist
class demo:
    a=10
ob=demo()
try:
    print(ob.b)
except:
    print("\nException occured")

#ii) Assertion error
print("\n")
a=1
b=0
try:
    assert b!=0,"Invalid operation"
except:
    print("End")

#iii) FileNotFoundError
print("\n")
fp=open("pqrs.txt","r")
try:
    print(fp.read())
except:
    print("File not found")
 
#iv) index error -> raised when index is out of range
print("\n")
l=[10,20,30]
try:
    print(l[10])
except:
    print("Index out of range")

#v) key error -> raised when we access a key which doesn't exist in dictionary
print("\n")
d={"ken":90,"kenny":80}
try:
    print(d["Brooklyn"])
except:
    print("Key not found")

#vi) ModuleNotFoundError -> raised when we import a module which doesn't exist
print("\n")
import bridge

#vii)NameError -> arises when name or identifier is accessed which doesn't exist
print("\n") 
a=10
b=20
print(a,b,c)

#viii) TypeError -> arises when operation are performed on unsupported data types
print("\n")
print(2 + "string")

#ix) ValueError -> arises when mistypecasting is performed on particular data on particular value
print("\n")
a="hello"
print(int(a))

# x) ZeroDivisionError
print("\n")
a=1
b=0
print(a/b)