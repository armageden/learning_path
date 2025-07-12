n, k = map(int, input().split())
a = list(map(int, input().split()))

max_len=    0
current_sum=0
l=0
#can I do it now????
for r in range(n):

    
    current_sum= current_sum+ a[r]
    # if current_sum < k:
    #     continue
    while current_sum > k:
        current_sum -= a[l]
        l += 1
    
    max_len = max(max_len, r-l+1)

print(max_len)