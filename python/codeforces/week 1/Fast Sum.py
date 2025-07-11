# This code solves the problem of calculating the sum of the first N natural numbers for multiple test cases.
#it is good for time compleity O(1) and space complexity O(1)
T=int(input())
for far in range(T):
    N=int(input())
    print((N*(N+1))//2)