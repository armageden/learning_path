import sys
from collections import deque
input=sys.stdin.readline
n,m,s,q=map(int,input().split())
a=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    a[u].append(v)
    a[v].append(u)
srcs=list(map(int,input().split()))
dsts=list(map(int,input().split()))
d=[-1]*(n+1)
qu=deque()
for src in srcs:
    if d[src]==-1:
        d[src]=0
        qu.append(src)
while qu:
    u=qu.popleft()
    for v in a[u]:
        if d[v]==-1:
            d[v]=d[u]+1
            qu.append(v)
res=[]
for dst in dsts:
    res.append(str(d[dst]))
print(" ".join(res))