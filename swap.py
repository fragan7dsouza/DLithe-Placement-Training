a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
print("before swapping: a=", a, "b=", b)
a=a+b
b=a-b
a=a-b
print("after swapping: a=", a, "b=", b)
