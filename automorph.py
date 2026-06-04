# num=int(input("enter a number:"))
# sq=num*num
# numstr= str(num)
# sqstr=str(sq)

# if sqstr.endswith(numstr):
#     print(num,"is automorphic")
# else:
#     print(num,"is not automorphic")

num=int(input("enter a number:"))
sq=num*num
temp=num
dig=1

while temp>0:
    dig*=10
    temp//=10
if sq%dig==num:
    print(num, "is automorphic")
else:
    print(num,"is not automorphic")

