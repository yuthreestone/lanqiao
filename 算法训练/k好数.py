strk,strl=input().strip().split()
k=int(strk)
l=int(strl)
dp=[[0 for i in range(l+1)] for j in range(k)]
if(l==0):
    print(0)
elif(l==1 and k==1):
    print(0)
elif(l==1):
    print(k)
else:
    for i in range(k):
        dp[i][1]=1
    j=1
    while j<l:
        j+=1
        for i in range(k):
            for m in range(k):
                if m!=i-1 and m!=i+1:
                    dp[i][j]+=dp[m][j-1]
                    dp[i][j]%=1000000007
    ans=0
    for i in range(k):
        if i!=0:
            ans+=dp[i][l]
            ans%=1000000007
    print(ans)
