# # #    *
# # #   **
# # #  ***
# # # ****

# # n = int(input("enter number of rows: "))
# # for i in range(1, n+1):
# #     spaces = n - i
# #     stars = i
# #     print(" " * spaces + "*" * stars)


# n = int(input("enter number of rows: "))
# for i in range(n, 0, -1):
#     spaces = n - i
#     stars = i
#     print(" " * spaces + "*" * stars)

n = int(input("enter size: "))
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")

