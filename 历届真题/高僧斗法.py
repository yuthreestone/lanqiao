listLoc=list(map(int,input().strip().split()))
n=len(listLoc)
if n==1:
    print(-1)
elif n==2:
    if listLoc[0]+1==listLoc[1]:
        print(-1)
    else:
        print(listLoc[0],end=" ")
        print(listLoc[1]-1)
else:
    dis=[]
    for i in range(n-1):
        dis.append(listLoc[i+1]-listLoc[i]-1)

    xor=dis[0]
    if n==3:
        if xor==0:
            print(-1)
        else:
            print(listLoc[0],end=" ")
            print(listLoc[1]-1)

    for i in range(2,len(dis),2):
        xor^=dis[i]
    if xor==0:
        print(-1)
    else:
        for j in range(n-1):
            disrange=dis[j]
            for k in range(disrange):
                dis[j]-=k
                if not j==0:
                    dis[j-1]+=k
                xor=dis[0]
                for p in range(2,len(dis),2):
                    xor^=dis[p]
                if xor==0:
                    print(listLoc[j],end=" ")
                    print(listLoc[j]+k)
                    exit(0)
                else:
                    dis[j]+=k
                    if not j==0:
                        dis[j-1]-=k
                
