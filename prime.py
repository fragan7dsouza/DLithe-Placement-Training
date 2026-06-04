n=int(input("enter a number:"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag+=1
if(flag==0):
    print("prime")
else:
    print("not prime")
    