listlv=[0]*5
listw=[[0 for i in range(8)]for i in range(5)]
listl=[0]*5
listp=[0]*5

#先用列表listlv存储各个等级的装饰孔的数量（例如，listlv[1]=3表示等级为1的装饰孔共3个）
for i in range(6):
    listinput=list(map(int,input().split()))
    for i in range(1,len(listinput)):
        listlv[listinput[i]]+=1

summ=0

m=int(input())
for i in range(m):
    listt=list(map(int,input().split()))
    listl[listt[0]]=listt[0]
    listp[listt[0]]=listt[1]
    listw[listt[0]]=[0]+listt[2:]

#按等级从大到小，对于每种等级的装饰珠进行枚举
for i in range(min(listlv[4],listp[4])+1):
    for j in range(min(listlv[4]+listlv[3]-i,listp[3])+1):
        for k in range(min(listlv[4]+listlv[3]+listlv[2]-j-i,listp[2])+1):
            for l in range(min(listlv[4]+listlv[3]+listlv[2]+listlv[1]-j-i-k,listp[1])+1):
                summ=max(summ,listw[4][i]+listw[3][j]+listw[2][k]+listw[1][l])

print(summ)

