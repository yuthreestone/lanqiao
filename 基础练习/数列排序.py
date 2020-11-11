num=int(input().strip())
list1=list(map(int,input().strip().split()))
list1.sort()
for i in list1:
    print(i,end=" ")
print("")
