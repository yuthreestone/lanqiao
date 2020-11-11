num=int(input())
listNum=[int(i) for i in input().split()]

count=0
for i in range(num-1):
    maxnum=minnum=listNum[i]
    for j in range(i+1,num):
        if listNum[j]<minnum:
            minnum=listNum[j]
        elif listNum[j]>maxnum:
            maxnum=listNum[j]                      
        if maxnum-minnum==j-i:
            count+=1
      
print(count+num)

#第五个评测点运行超时
