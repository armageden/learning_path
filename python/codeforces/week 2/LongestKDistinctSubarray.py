N,K=map(int,input().split())
arr=list(map(int, input().split()))
flag=True
left=0
ans=0
freq = {}
# alright gigidy gigigy
for right in range(N):

    freq[arr[right]] = freq.get(arr[right],0)+1
    
    while len(freq) > K:
        freq[arr[left]] -=1
        if freq[arr[left]]==0:
            del freq[arr[left]] # this is the final draw... then I am leaving it blank
        left = left + 1



    ans=max(ans,right-left+1)

print(ans)