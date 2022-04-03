#there are 11 dictionary methods 

d={1:'A',2:'B',3:'C'}
print(d)

#i) copy()
print("\n")
d1=d.copy()#copies the elements of dictionary from d to d1
print(d1)

#ii) clear()
print("\n")
d.clear()#removes all element of dictionary and returns a empty dictionary
print(d)

#iii) get()
print("\n")
d2={1:'a',2:'b',3:'c'}
print(d2.get(2))#returns the value as output using key value

#iv) items()
print("\n")
d3={1:'a',2:'b',3:'c'}
print(d3.items())#returns list of items 

#v)keys()
print("\n")
d4={1:'a',2:'b',3:'c'}
print(d4.keys())#returns list of keys

#vi) values()
print("\n")
d5={1:'a',2:'b',3:'c'}
print(d5.values())#returns list of values

#vii) update()
print("\n")
d6={1:'a',2:'b',3:'c'}
d6.update({'Name':'Zeo','Roll':10})#adds more than 1 item
print(d6)

#viii) pop()
print("\n")
d7={1:'a',2:'b',3:'c'}
print(d7.pop(1))#removes the given element as done by user....here it is 'a'
print(d7)

#ix) popitem()
print("\n")
d8={1:'a',2:'b',3:'c'}
print(d8.popitem())#deletes the last inserted element 
print(d8)

#x) setdefault()
print("\n")
d9={1:'a',2:'b',3:'c'}
d9.setdefault(4,'d')
print(d9)

#xi) fromkeys()
print("\n")
d10={1:'a',2:'b',3:'c'}
k=(1,2,3)
d10=d10.fromkeys(k,'python')
print(d10)