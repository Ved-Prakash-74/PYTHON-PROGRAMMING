#python program for break, continue and pass statements

#break statement
i=1
while(i<=10):
    print(i)
    if(i==5):
        break
    i=i+1

#continue statement
print("\n")
for i in range(1,11,1):
    if(i==5):
        continue
    print(i)

#pass
print("\n")
for i in range(1,5,1):
    if(i%2==0):
        print(i)
    else:
        pass