import copy
list1=[1]*34
num=int(input().strip())
i=1
while(i<=num):
    print(1,end=" ")
    j=1
    list2=copy.deepcopy(list1)
    while(j<i-1):

        list1[j]=list2[j-1]+list2[j]
        print(list1[j],end=" ")
        j+=1
    if(i>1):
        print(1)
    else:
        print("")
    i+=1
