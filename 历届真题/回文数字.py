def rev(n):
    a=str(n)
    b=a[::-1]
    if b==a:
        return True
    else:
        return False

def total(n,num):
    add=0
    while n>0:
        add+=n%10
        n//=10
    if add==num:
        return True
    else:
        return False


num=int(input())
count=0
for i in range(10000,1000000):
    if rev(i):
        if total(i,num):
            count+=1
            print(i)
        
if count==0:
    print(-1)

