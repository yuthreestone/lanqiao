a,b=input().strip().split()
n=int(a)
m=int(b)
#ord('A')=65
i=1
while(i<=n):
    j=1
    while(j<=i and j<=m):
        print(chr(65+i-j),end="")
        j+=1
    if(j<=m):
        while(j<=m):           
            print(chr(65+j-i),end="")
            j+=1
    print("")
    i+=1
