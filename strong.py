num=int(input("enter number:"))
temp=num
sum=0
while num>0:
    fact=1
    d=num%10
    for i in range(1,d+1):
        fact=fact*i
    sum+=fact
    num=num//10
if sum==temp:
    print("strong number")
else:
    print("not strong number")
