def rev(n):
    a=str(n)
    b=a[::-1]
    if b==a:
        return True
    else:
        return False

for i in range(1000,10000):
    if rev(i):
        print(i)
