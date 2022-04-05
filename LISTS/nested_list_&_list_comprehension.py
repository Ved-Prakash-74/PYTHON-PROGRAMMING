#nested list
l1=[10,2.5,True,["a",20,"b"]]
print(l1[0])
print(l1[3])
print(l1[3][0])
print(l1[3][1])
print(l1[3][2])

l2=[[[10,20],[30,40]],[[50,60],[70,80]]]
print(len(l2))
print(l2[0])
print(l2[1])
print(l2[0][0])
print(l2[0][1])
print(l2[0][0][0])
print(l2[0][0][1])

#list comprehension
#it is used to reduce lines of codes
#syntax  1-------->>>>>  l=[expression for var in sequence]
#syntax  2-------->>>>>  l=[expression for var in sequence if condition]
#let's understand it with example 
#cube of number from 1 to 10 using syntax 1
print("\n")
l3=[i**3 for i in range(1,11)]
print(l3)
#print even number from 1 to 10 using syntax 2
l4=[i for i in range(1,11) if i%2==0] 
print(l4) 