#There are 12 basic operations on list

l=[10,20,30,40,50] 
print(l)

#i) len()
print(len(l))#prints the lenght of list

#ii) concatenation
l1=[60,70]
l2=l+l1#adds elements of l1 at end of l
print(l2)

#iii) repetition
print(l1*2)#repeates elements of list to given number of times

#iv)in
if 10 in l:#checks whether given element is in list or not....returns true if present else false
    print("True")
else:
    print("False")

#v) not in
if 100 not in l:#checks whether given element is not present in list....returns true if not present else false
    print("true")
else:
    print("false")

#vi) max()
print(max(l))#returns max element from list

#vii) min()
print(min(l))#returns min element from list

#viii) sum()
print(sum(l))#returns sum of all element 

#ix) all()
print(all(l))#checks whether all element in are non zero value or not

#x) any()
print(any(l))#checks whether any of the element in list is non zero value or not

#xi)list()
s="Hii"
l4=list(s)#converts to list from other data type list tuple, set
print(l4)

#xii) sorted()
l5=[50,40,20,30,80,10,70,60]
print(sorted(l5))