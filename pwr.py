# num=int(input("enter a number:"))
# if num>0 and (num&(num-1))==0:
#     print(num,"is a power of 2")
# else:
#     print(num,"is not power of 2")


num=int(input("enter a number:"))
while num:
    if num==1:
        print("power of 2")
        break
    if num%2==0:
        num=num//2
    elif num%2!=0:
        print("not power of 2")
        break
