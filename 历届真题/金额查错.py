import copy
import operator
wrongm=int(input())
n=int(input())
listn=[]
listm=[]
count=0
listlast=[]

for i in range(n):
    listn.append(int(input()))

summ=sum(listn)

summ-=wrongm

listn.sort()

def dfs(i):
    global listm,listn,summ,n,setans,listlast
    #print(i,end=' ')
    #print(listn,summ)
    #print(listm)
    if summ==0:
        if not operator.eq(listm,listlast):
            for i in range(len(listm)):
                print(listm[i],end=' ')
            print('')
            listlast=copy.deepcopy(listm)  #深拷贝
    elif i==n:
        return
    elif summ>=listn[i]:
        listm.append(listn[i])
        summ-=listn[i]
        dfs(i+1)
        summ+=listn[i]
        listm.pop()
        dfs(i+1)
    else:
        dfs(i+1)

dfs(0)

