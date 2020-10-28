stra,strb,strc=input().strip().split()
a=int(stra)
b=int(strb)
c=int(strc)
for i in range(1,27000):
    if i%a==0:
        if i%b==0:
            if i%c==0:
                print(i)
                break;
            else:
                continue;
        else:
            continue;
    else:
        continue;

