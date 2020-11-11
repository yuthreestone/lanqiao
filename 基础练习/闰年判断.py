year=int(input().strip())
if(year%400==0):
    print("yes")
else:
    if(year%4==0 and year%100!=0):
        print("yes")
    else:
        print("no")
