num=int(input().strip())
list1=list(map(int,input().strip().split()))
findnum=int(input().strip())
if(findnum in list1):
    print(list1.index(findnum)+1)
else:
    print(-1)
