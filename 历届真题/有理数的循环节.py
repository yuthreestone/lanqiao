listans=[0]*200
listindex=[0]*200


a,b=map(int,input().split(','))
print(a//b,end='')
a%=b

for i in range(1,200):
    if a==0:
        if i!=1:
            print('.',end='')
        for j in range(1,i):
            print(listans[j],end='')
        break

    if listindex[a]==0:
        listindex[a]=i

    else:
        print('.',end='')
        for j in range(1,i):
          if j==listindex[a]:
              print('[',end='')
          print(listans[j],end='')
        print(']')
        break
    a*=10
    listans[i]=a//b
    a%=b
