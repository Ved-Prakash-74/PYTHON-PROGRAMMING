# accessing, slicing, deleting and nested tuple

t=(10,20,30,40,50)
print(t)

#accessing
print("\n")
print(t[0])
print(t[1])
print(t[-1])
print(t[-2])

#slicing
print("\n")
print(t[0:4])
print(t[0:4:2])
print(t[2:])
print(t[:4])
print(t[-4:])

#deleting
print("\n")
#element can't be deleted but entire tuple can
del t

#nested tuple
print("\n")
t=(10,20,(30,40))
print(t)
print(t[0])
print(t[2])
print(t[2][0])
print(t[2][1])