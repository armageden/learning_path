import sys
import heapq

def solve():
    n,m,s,t=map(int,sys.stdin.readline().split())
    adj=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w=map(int,sys.stdin.readline().split())
        adj[u].append((v,w))
    inf=float('inf')
    def dijkstra(start,dists):
        #ami ki parbo re vai?
        for i in range(n+1):
            dists[i]=inf
        dists[start]=0
        pq=[(0,start)]
        while pq:
            d,u=heapq.heappop(pq)
            if d>dists[u]:
                continue
            for v,w in adj[u]:
                if dists[u]+w<dists[v]:
                    dists[v]=dists[u]+w
                    heapq.heappush(pq,(dists[v],v))
    ds=[0]*(n+1)
    dt=[0]*(n+1)
    dijkstra(s,ds)
    #valo lage na re
    dijkstra(t,dt)
    mt=inf
    mn=-1
    for i in range(1,n+1):
        if ds[i]!=inf and dt[i]!=inf:
            ct=max(ds[i],dt[i])
            if ct<mt:
                mt=ct
                mn=i
    if mn==-1:
        print(-1)
    else:
        print(mt,mn) #r akorbo na

solve()