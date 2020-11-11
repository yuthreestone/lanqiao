def sumequal(str1,n):
    summ=0
    i=0
    while(i<len(str1)):
        summ+=int(str1[i])
        i+=1
    if(n==summ):
        return True
    else:
        return False

def check(num,n):
    str1=str(num)
    if equal(str1,str1[::-1]):
        if(sumequal(str1,n)):
            return True
        else:
            return False
    else:
        return False

def equal(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    else:
        i=0
        while(i<len(str1)):
            if(str1[i]!=str2[i]):
                return False
            i+=1
        return True


n=int(input().strip())
i=10000
while(i<1000000):
    if(check(i,n)):
        print(i)
    i+=1
