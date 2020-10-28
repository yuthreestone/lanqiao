num=int(input().strip())
width=4*num+5
listsav=[[0 for i in range(width)]for j in range(width)]

#标记中心的十字
mid=width//2
for i in range(mid-2,mid+3):
    listsav[i][mid]=listsav[mid][i]=1

#从外层到内层标记$圈
for i in range(num,0,-1):
    ordinal=num-i+1
    for j in range(2*ordinal,width-2*ordinal):
        listsav[2*ordinal-2][j]=listsav[width-2*ordinal+1][j]=1
        listsav[j][2*ordinal-2]=listsav[j][width-2*ordinal+1]=1
    for j in range(2*ordinal-1,2*ordinal+1):
        for k in range(2*ordinal-1,2*ordinal+1):
            if not(j==k and j==2*ordinal-1):
                listsav[j][k]=listsav[j][width-k-1]=1
                listsav[width-j-1][k]=listsav[width-j-1][width-k-1]=1

#打印图形
for i in range(width):
    for j in range(width):
        if listsav[i][j]==0:
            print(".",end="")
        else:
            print("$",end="")
    print("")
            

