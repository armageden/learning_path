n,m,k=map(int,input().split())
arre1=list(map(int,input().split()))
arre2=list(map(int,input().split()))
i,j=0,m-1
i_res,j_res=0,0
lowst_diff=float('inf') #FOR INFINITY AS NEED GRETEST NUMBER
while i<n and j>=0:
    sum_cur=arre1[i]+arre2[j]
    dif=abs(k-sum_cur)
    if dif<lowst_diff:
        lowst_diff=dif
        i_res,j_res=i,j
    elif dif==lowst_diff:
        pass
    if sum_cur>k:
        j-=1
    elif sum_cur<k:
        i+=1
    else:
        break
print(i_res+1, j_res+1)