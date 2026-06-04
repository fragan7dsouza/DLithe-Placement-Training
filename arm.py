num= int(input("enter a number:"))
temp=num
sum=0
n=len(str(num))

while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if num==sum:
    print(num, "is armstrong number")
else:
    print(num, "isnt armstrong number")
    