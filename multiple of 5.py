n=list(map(int,input("enter multiple values:").split(',')))
for i in n:
    if i%5==0:
        i-=5
    print(i,end=' ')  
