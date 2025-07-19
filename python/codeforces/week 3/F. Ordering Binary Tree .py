n=int(input())
a=list(map(int,input().split()))
res=[]
def build_order(arr,low,high):
    # left right
    if low > high:
        return
    mid = (low + high) // 2
    res.append(arr[mid])
    #hmmmmm this is a binary tree......
    build_order(arr,low,mid-1)
    build_order(arr,mid+1,high)
build_order(a,0,n-1)
print(*res)
#better than brute force method