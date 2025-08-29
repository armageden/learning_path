import heapq
import sys

def solve():
    n,m=map(int,sys.stdin.readline().split())
    adj=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w=map(int,sys.stdin.readline().split())
        adj[u].append((v,w))
        adj[v].append((u,w))

    danger=[float('inf')]*(n+1)
    danger[1]=0
    pq=[(0,1)]

    while pq:
        d,u=heapq.heappop(pq)
        if d>danger[u]:
            continue
        for v,w in adj[u]:
            new_danger=max(d,w)
            if new_danger<danger[v]:
                danger[v]=new_danger
                heapq.heappush(pq,(new_danger,v))

    for i in range(1,n+1):
        if danger[i]==float('inf'):
            print(-1,end=' ')
        else:
            print(danger[i],end=' ')
    print()

solve()