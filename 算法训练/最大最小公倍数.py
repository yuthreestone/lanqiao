n=int(input().strip())
if n%2==1:
    print(n*(n-1)*(n-2))
elif n%3==0:
    print((n-1)*(n-2)*(n-3))
else:
    print(n*(n-1)*(n-3))
