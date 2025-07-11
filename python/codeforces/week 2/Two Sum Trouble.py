N,S=map(int,input().split())
flag=False
arre1=list(map(int,input().split()))
l_p,r_p=0,N-1
while l_p<r_p:#(maybe <= is good or not?? try here goes test...)
    if arre1[l_p]+arre1[r_p]==S:
        print(l_p+1, r_p+1)
        break
    elif arre1[l_p]+arre1[r_p]<S:
        l_p+=1
    else:
        r_p-=1
    
#should I put a if? ...no ig
else: 
    print(-1)

