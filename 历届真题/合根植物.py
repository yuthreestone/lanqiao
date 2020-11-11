global pre

def find(x):
    while(x!=pre[x]):
        x=pre[x]
    return x

strm,strn=input().strip().split()
m=int(strm)
n=int(strn)
pre=[i for i in range(m*n+1)]
allnum=m*n
count=int(input().strip())
index=0
while(index<count):
    index+=1
    stra,strb=input().strip().split()
    roota=find(int(stra))
    rootb=find(int(strb))
    if roota!=rootb:
        pre[roota]=rootb
        allnum-=1
print(allnum)
