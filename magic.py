# num = int(input("enter a number: "))
# temp = num

# while temp >= 10:
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit
#         temp //= 10
#     temp = sum

# if temp == 1:
#     print(num, "is magic")
# else:
#     print(num, "not magic")

num = int(input("enter a number: "))
temp = num

while temp >= 10:
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10
    temp = sum

if temp == 1:
    print(num, "is magic")
else:
    print(num, "not magic")