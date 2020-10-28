num=int(input().strip())

def check(num):
    flag=[0]*10
    while num!=0:
        tail=num%10
        if tail==0:
            return False
        flag[tail]+=1
        num=num//10
    if flag[0]>0:
        return False
    for i in range(1,10):
        if flag[i]>1:
            return False
    return True

def checkAll(left,up,down):
    flag=[0]*10
    while left!=0:
        tail=left%10
        if tail==0:
            return False
        if flag[tail]>0:
            return False
        flag[tail]+=1
        left=left//10
    while up!=0:
        tail=up%10
        if tail==0:
            return False
        if flag[tail]>0:
            return False
        flag[tail]+=1
        up=up//10
    while down!=0:
        tail=down%10
        if tail==0:
            return False
        if flag[tail]>0:
            return False
        flag[tail]+=1
        down=down//10
    for i in range(1,10):
        if flag[i]==0:
            return False
    return True

for i in range(1,num):
    
