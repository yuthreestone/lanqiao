n=int(input())
summ=0
listsav=[[0 for i in range(n)]for j in range(n)]
flag=0
maxn=0
summ=0

for i in range(n):
    listsav[i]=list(map(int,input().split()))

def dpp(row,col):   
    global flag,summ,maxn
    if row==n-1:
        summ+=listsav[row][col]
        if abs(flag)<2 and summ>maxn:
            maxn=summ
        summ-=listsav[row][col]
    else:
        summ+=listsav[row][col]
        flag-=1
        dpp(row+1,col)
        flag+=2
        dpp(row+1,col+1)
        summ-=listsav[row][col]
        flag-=1


dpp(0,0)
print(maxn)
