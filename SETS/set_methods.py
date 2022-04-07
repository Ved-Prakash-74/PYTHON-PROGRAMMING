#there are 15 set methods

from ctypes import Union


s={10,20,30,40,50}
print(s)

#i) add()
print("\n")
s.add(60)#adds a single element to set
print(s)

#ii) update()
print("\n")
s1={70,80}
s.update(s1)#adds more than 1 element to set
print(s)

#iii) remove()
print("\n")
s.remove(80)#removes 80 from set
print(s)

#iv) discard()
print("\n")
s.discard(70)
print(s)

#both remove() and discard() deletes single element from set....but the difference is in case of remove()
#if we try to delete the element which is not present in set it gives the error message while on the other 
#hand in discard() no suvh error message while occur

#v) pop()
print("\n")
s.pop()#any element can be deleted from set as there is no indexing
print(s)

#vi) clear()
print("\n")
s2={10,20,30,40,50}
s2=s2.clear()#all elements of set are removed or cleared
print(s2)

#vii) del()
print("\n")
s3={10,20,30}
del s3#deletes entire set 

#viii) union()
print("\n")
s4={10,20,30,40}
s5={30,40,50,60}
s4=s4.union(s5)#elements from both the sets are merged to single set except common elements
print(s4)

#ix) intersecton()
print("\n")
s6={10,20,30,40}
s7={30,40,50,60}
s6=s6.intersection(s7)#common elements from both the sets are merged to single set
print(s6)

#x)difference()
print("\n")
s8={10,20,30,40}
s9={30,40,50,60}
s8=s8.difference(s9)#prints all elements of s8 except those which are common to s9
s9=s9.difference(s8)#prints all elements of s9 except those which are common to s8
print(s8)
print(s9)

#xi) symmetric_difference
print("\n")
s10={10,20,30}
s11={20,30,50}
s10=s10.symmetric_difference(s11)#prints all elements of both sets except those which are common in both sets
print(s10)

#xii) issubset()
print("\n")
s12={10,20,30,40}
s13={20,10,50,40}
print(s12.issubset(s13))#if all elements of s12 is present in s13 then it returns true else false
print(s13.issubset(s12))#if all elements of s13 is present in s12 then it returns true else false

#xiii) issuperset()
print("\n")
s14={10,20,30,40}
s15={10,20,30,40}
print(s14.issuperset(s15))#if all elements of s14 is present in s15 then it returns true else false

#xiv) isdisjoint()
print("\n")
s16={10,20,30,40}
s17={50,60,70,80}
print(s16.isdisjoint(s17))#if there are no common elements in set then it returns true else false

#xv) copy()
print("\n")
s18={10,20,30,40}
s19=s18.copy()#copies all element of one set to another set
print(s19)
