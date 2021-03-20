n,m,k,t=map(int,input().split())
listt=list(map(int,input().split()))
listk=list(map(int,input().split()))
listm=[[]for i in range(n+1)]
listt.insert(0,0)
dp=[100]*(n+1)
for i in range(k):
    a,b,c=map(int,input().split())
    listm[c].append([a,b])

for i in range(m):
    dp[listk[i]]=0

def ddp(num):
    global dp,listm,listt,listk
    if num in listk:
        return 0
    minn=10000
    for i in range(len(listm[num])):
        summ=max(ddp(listm[num][i][0]),ddp(listm[num][i][1]))+max(listt[listm[num][i][0]],listt[listm[num][i][1]])
        if summ<minn:
            minn=summ
    dp[num]=minn
    return dp[num]

print(ddp(t))
