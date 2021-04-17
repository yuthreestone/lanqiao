string=input()
num=int(input())
dicty={}
numdicty={}

def handle(string):
    liststring=list(string)
    liststring.sort()
    string=""
    for i in range(len(liststring)):
        string+=liststring[i]
    return string

for i in range(num):
    strr=input()   
    handled=handle(strr)   

    if handled in dicty:
        dicty[handled]+=1
    else:
        dicty[handled]=1

ans=0
for i in range(len(string)-7):
    strrr=string[i:i+8]
    hstr=handle(strrr)
    if hstr in dicty:
        ans+=dicty[hstr]

print(ans)
        
