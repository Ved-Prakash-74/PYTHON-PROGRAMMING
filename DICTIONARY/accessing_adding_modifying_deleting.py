#accessing, adding, modifying and deleting dictionary items

d={1:'A',2:'B',3:'C'}
print(d)

#i) accessing
print(d[1])
print(d[2])

#ii) adding
d[4]='D'
print(d)

#iii) modifying
d[1]='E'
print(d)

#iv) deleting
del d[1]
print(d)
del d#deletes entire dictionary....so it can't be printed as it will give an error