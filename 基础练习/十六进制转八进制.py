n=int(input().strip())
i=0
while i<n:
    num=input().strip()
    print(oct(int(num,16))[2:]) #去掉八进制的前缀0o
    i+=1
