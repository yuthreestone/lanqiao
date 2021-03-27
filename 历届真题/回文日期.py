def isvalid(num):
    year=num//10000
    num%=10000
    month=num//100
    num%=100
    day=num
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and day<32:
        return True
    if (month==4 or month==6 or month==9 or month==11) and day<31:
        return True
    if (month==2 and day<29):
        return True
    if month==2:
        if year%400==0:
            if day==29:
                return True
        if year%4==0 and not year%100==0:
            if day==29:
                return True
    return False


def isrev(num):
    strnum=str(num)
    if strnum==strnum[::-1]:
        return True
    return False

num=int(input())
for i in range(num+1,89991232):
    if (isrev(i) and isvalid(i)):
        print(i)
        break

if (isrev(num) and isvalid(num)):
    item=num//1000000+1
else:
    item=num//1000000
for i in range(item,81):
    A=i//10
    B=i%10
    num=item*1010000+A*101+B*1010
    if (isrev(num) and isvalid(num)):
        print(num)
        break
