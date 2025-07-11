N=int(input())
arr1=list(map(int,input().split()))
on=0
while (on<N):
    off=on+1
    while(off<N and arr1[off]%2==arr1[on]%2):
        off+=1
    arr1[on:off]=sorted(arr1[on:off])
    on=off
print(*arr1)
