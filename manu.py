l=[6,2,5,5,4,5,6,3,7,6]
a=int(input())
b=int(input())
sum=a+b
total=0
while sum>0:
    digit=sum%10
    total+=l[digit]
    sum//=10
print("number of matchsticks:",total)
