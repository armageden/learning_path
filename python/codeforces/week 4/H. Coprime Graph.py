import sys
import math
input=sys.stdin.readline
n,q=map(int,input().split())
adj=[[] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i!=j and math.gcd(i,j)==1:
            adj[i].append(j)
for _ in range(q):
    x,k=map(int,input().split())
    if k<=len(adj[x]):
        print(adj[x][k-1])
    else:
        print(-1)
