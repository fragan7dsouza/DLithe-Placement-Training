p=int(input("enter a number:"))
q=0
for i in range(1,p):
    if(p%i)==0:
        q+=i
if q==p:
    print("perfect")
else:
    print("not perfect")
