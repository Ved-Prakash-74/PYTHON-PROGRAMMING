#there are 8 basic operations on sets

s={10,20,30,40,50}
print(s)

#i) len()
print(len(s))#prints the length of set

#ii) max()
print(max(s))#returns max value from set

#iii) min()
print(min(s))#returns min value from set

#iv) sum()
print(sum(s))#returns sum of all values from set

#v) sorted()
s1={30,50,10,40,20}
print(sorted(s))#prints set in sorted order

#vi) del ()
s2={30,50,10,40,20}
del s2#deletes the entire set

#vii) in()
if 30 in s:#checks whether the given num is in set or not....if present returns true else false
    print(True)
else:
    print(False)

#viii) not in ()
if 30 not in s:#checks whether the given num is in set or not....if not present returns true else false
    print(True)
else:
    print(False)