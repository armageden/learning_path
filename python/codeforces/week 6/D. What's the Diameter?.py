import sys
from collections import deque
input=sys.stdin.readline
def bfs(s,n,a):
    q=deque([s])
    d=[-1]*(n+1)
    d[s]=0
    while q:
        u=q.popleft()
        for v in a[u]:
            if d[v]==-1:
                d[v]=d[u]+1
                q.append(v)
    md=-1
    fn=-1
    for i in range(1,n+1):
        if d[i]>md:
            md=d[i]
            fn=i
    return md,fn
n=int(input())
a=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    a[u].append(v)
    a[v].append(u)
_,ea=bfs(1,n,a)
dl,eb=bfs(ea,n,a)
print(dl)
print(ea,eb)