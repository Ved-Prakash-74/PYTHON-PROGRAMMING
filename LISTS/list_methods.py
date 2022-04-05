#there are 9 list methods

l=[10,20,30,40,50]
print(l)

#i)append()
print("\n")
l.append(60)#adds a single element to last of list
print(l)

#ii)insert()
print("\n")
l.insert(2-1,100)#used to insert element any position in list.....here it is inserted at 2nd postion,,,,-1 as indexing starts from 0
print(l)

#iii)extend()
print("\n")
l.extend([70,80,90])#used to append more than one element in list
print(l)

#iv)remove()
print("\n")
l2=[10,20,20,30,40,50]
l2.remove(20)#removes the first occurence
print(l2)

#v)pop()
print("\n")
l.pop()#removes last element which is inserted in list
print(l)
l.pop(2-1)#popping can also be done using index value....here 2nd element is popped out,,,,-1 as indexing starts from 0
print(l)

#vi)count()
print("\n")
print(l.count(20))#counts how many times the same element is repeated

#vii)index()
print("\n")
print(l.index(20))#returns the index position of element....if element is repeated more than 1 time then index value of first occurence will be returned

#viii)reverse()
print("\n")
l.reverse()#used to reverse the given list
print(l)

#ix)sort()
print("\n")
l.sort()
print(l)