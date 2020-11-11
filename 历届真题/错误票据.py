listNum=[]
n=int(input().strip())
for i in range(n):
    listNum.extend(list(map(int,input().strip().split())))

listNum.sort()
baseNum=listNum[0]
for i in range(len(listNum)):
    if listNum.count(listNum[i])==2:
        renum=listNum[i]
    if baseNum+i not in listNum:
        nonum=baseNum+i

print(nonum,renum)

