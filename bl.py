bob,limak = map(int,input("enter:").split())
years=0
while bob<=limak:
    bob=bob*3
    limak=limak*2
    years+=1
print(years)
