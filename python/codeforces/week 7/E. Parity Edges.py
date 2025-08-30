import heapq
import sys

def solve():
    n,m=map(int,sys.stdin.readline().split())
    u=list(map(int,sys.stdin.readline().split()))
    v=list(map(int,sys.stdin.readline().split()))
    w=list(map(int,sys.stdin.readline().split()))
    adj=[[] for _ in range(n+1)]
    for i in range(m):
        adj[u[i]].append((v[i],w[i]))
    dist=[[float('inf'),float('inf')] for _ in range(n+1)]
    pq=[]
    for i in range(m):
        if u[i]==1:
            parity=w[i]%2
            if w[i]<dist[v[i]][parity]:
                dist[v[i]][parity]=w[i]
                heapq.heappush(pq,(w[i],v[i],parity))
    while pq:
        cost,curr,parity=heapq.heappop(pq)
        if cost>dist[curr][parity]:
            continue
        for neighbor,weight in adj[curr]:
            new_cost=cost+weight
            new_parity=weight%2
            if new_parity!=-1 and new_parity!=parity and new_cost<dist[neighbor][new_parity]:
                dist[neighbor][new_parity]=new_cost
                heapq.heappush(pq,(new_cost,neighbor,new_parity))
    result=min(dist[n])
    if result==float('inf'):
        print(-1)
    else:
        print(result)

solve()