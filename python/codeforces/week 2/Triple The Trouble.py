n,bingo=map(int,input().split())
arre1=list(map(int,input().split()))
probe=[] #to see the results
flag=False

ind_a=[]
for i in range(n):
    ind_a.append((arre1[i], i + 1))
    #damn it needs sort now? 
ind_a.sort()
for far in range(n):
    notun=bingo-ind_a[far][0]
    l_p=far+1
    r_p=n-1
    
    while l_p<r_p:



        pres=ind_a[l_p][0]+ind_a[r_p][0]
        if pres==notun:
            print(ind_a[far][1], ind_a[l_p][1], ind_a[r_p][1])
            flag=True
            break
        elif pres<notun:
            l_p+=1
        else:
            r_p-=1
    if flag:
        break
if not flag:
    print(-1)   