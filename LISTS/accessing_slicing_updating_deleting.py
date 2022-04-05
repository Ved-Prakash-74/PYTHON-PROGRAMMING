#performing accessing, slicing, updating, deltion operation on list

from re import L


l=[10,20,30,40,50]
print(l)

#accessing
print("\n")
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])

#slicing
print("\n")
print(l[0:4:1])
print(l[0:5:2])
print(l[2::])
print(l[:4:])
print(l[::])

#updating
print("\n")
l.append(60)#adds item to last
print(l)
l[0]=30
print(l)

#deletion
print("\n")
l.remove(30)#removes the first occurence of element
print(l)
print(l.pop())#removes the last element which is added
print(l.pop(2))#removes element which is at index 2
del l[1]#deletes element at index 1
print(l)
del l#deletes entire list
l1=[10,20,30,40,50]
del l1[1:3]#last index will not counted 
print(l1)