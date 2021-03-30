# 问题描述
#
# 　　学霸抢走了大家的作业，班长为了帮同学们找回 作业，决定去找学霸决斗。但学霸为了不要别人打扰，住在一个城堡里，城堡外面是一个二维的格子迷宫，要进城堡必须得先通过迷宫。因为班长还有妹子要陪，磨 刀不误砍柴功，他为了节约时间，从线人那里搞到了迷宫的地图，准备提前计算最短的路线。可是他现在正向妹子解释这件事情，于是就委托你帮他找一条最短的路 线。
#
# 输入格式
#
# 　　第一行两个整数n， m，为迷宫的长宽。
# 　　接下来n行，每行m个数，数之间没有间隔，为0或1中的一个。0表示这个格子可以通过，1表示不可以。假设你现在已经在迷宫坐标(1,1)的地方，即 左上角，迷宫的出口在(n,m)。每次移动时只能向上下左右4个方向移动到另外一个可以通过的格子里，每次移动算一步。数据保证(1,1)，(n,m)可 以通过。
#
# 输出格式
#
# 　　第一行一个数为需要的最少步数K。
# 　　第二行K个字符，每个字符∈{U,D,L,R},分别表示上下左右。如果有多条长度相同的最短路径，选择在此表示方法下字典序最小的一个。
#
# 样例输入
#
# Input Sample 1:
# 3 3
# 001
# 100
# 110
#
# Input Sample 2:
# 3 3
# 000
# 000
# 000
#
# 样例输出
#
# Output Sample 1:
# 4
# RDRD
#
# Output Sample 2:
# 4
# DDRR
#
# 数据规模和约定
#
# 　　有20%的数据满足：1<=n,m<=10
# 　　有50%的数据满足：1<=n,m<=50
# 　　有100%的数据满足：1<=n,m<=500。
n,m=map(int,input().split())
listsav=[[0 for i in range(m)]for j in range(n)]
listqu=[[0,0]]

def valid(a,b):
    global n,m
    if a>=0 and a<n and b>=0 and b<m:
        return True
    return False

for i in range(n):
    listsav[i]=list(input())

while len(listqu)>0:   #u d l r
    a=listqu[0][0]     #5 2 3 4
    b=listqu[0][1]
    listqu.pop(0)
    if valid(a+1,b):
        if listsav[a+1][b]=='0':
            listsav[a+1][b]='2'
            listqu.append([a+1,b])
            if a+1==n-1 and b==m-1:
                break
    if valid(a,b-1) and listsav[a][b-1]=='0':
        listsav[a][b-1]='3'
        listqu.append([a,b-1])
        if a==n-1 and b-1==m-1:
            break
    if valid(a,b+1) and listsav[a][b+1]=='0':
        listsav[a][b+1]='4'
        listqu.append([a,b+1])
        if a==n-1 and b-1==m-1:
            break
    if valid(a-1,b) and listsav[a-1][b]=='0':
        listsav[a-1][b]='5'
        listqu.append([a-1,b])
        if a-1==n-1 and b==m-1:
            break
    
listans=[]
sumlen=0
a=n-1
b=m-1
while True:
    if a==0 and b==0:
        break
    if listsav[a][b]=='2':
        listans.append('D')
        a-=1
        sumlen+=1
        continue
    if listsav[a][b]=='3':
        listans.append('L')
        b+=1
        sumlen+=1
        continue
    if listsav[a][b]=='4':
        listans.append('R')
        b-=1
        sumlen+=1
        continue
    if listsav[a][b]=='5':
        listans.append('U')
        a+=1
        sumlen+=1
        continue

print(sumlen)
for i in range(len(listans)-1,-1,-1):
    print(listans[i],end='')
