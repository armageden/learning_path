N=int(input())
arr1=list(map(int,input().split()))
if sorted(arr1[0::2])==sorted(arr1)[0::2] and sorted(arr1[1::2])==sorted(arr1)[1::2]:
    print("YES")
else:
    print("NO")