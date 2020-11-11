def check(num):
    str1=str(num)
    if equal(str1,str1[::-1]):
        return True
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



i=1000
while(i<10000):
    if(check(i)):
        print(i)
    i+=1
