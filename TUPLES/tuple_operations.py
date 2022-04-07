#there are 12 tuple operations

t=(10,20,30,40,50)
print(t)

#i) len()
print("\n")
print(len(t))#prints lenght of tuple

#ii) max()
print("\n")
print(max(t))#returns max element from tuple

#iii) min()
print("\n")
print(min(t))#returns min element from tuple

#iv) sum()
print("\n")
print(sum(t))#adds all element in tuple and returns it

#v) concatenation()
print("\n")
t1=(10,20,30)
t2=(40,50)
t3=t1+t2#adds t1 with t2
print(t3)

#vi) repetition()
print("\n")
t4=(40,50,5,2)
print(t4*2)#repeates elements of t2 2 times

#vii) in
print("\n")
if 10 in t:#checks whether the given element is present in tuple or not....returns true if present else false
    print("true")
else:
    print("false")

#viii) not in
print("\n")
if 100 not in t:#checks whether the given element is present in tuple or not....returns true if not present else false
    print("true")
else:
    print("false")

#ix) sorted()
print("\n")
t5=(40,50,5,2)
print(sorted(t5))#sorts all element of tuple

#x) tuple
print("\n")
s="hii"
t6=tuple(s)#converts to tuple from other data type like string, list
print(t6)

#xi) count()
print("\n")
t7=(10,20,10,30,40,10,50,10)
print(t7.count(10))#counts how many times the same number is repeated in tuple 

#xii) index()
print("\n")
t8=(10,20,10,30,40,10,50,10)
print(t8.index(10))#returns index of first occurence 