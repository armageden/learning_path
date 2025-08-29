import heapq
import sys

def solve():
    n,m,s,d=map(int,sys.stdin.readline().split())
    w=list(map(int,sys.stdin.readline().split()))
    adj=[[] for _ in range(n+1)]
    for _ in range(m):
        u,v=map(int,sys.stdin.readline().split())
        adj[u].append(v)
    
    dist=[float('inf')]*(n+1)
    
    if s==d:
        print(w[s-1])
        return
        
    dist[s]=w[s-1]
    pq=[(w[s-1],s)]

    while pq:
        cost,u=heapq.heappop(pq)
        
        if u==d:
            print(cost)
            return
            
        if cost>dist[u]:
            continue

        for v in adj[u]:
            new_cost=cost+w[v-1]
            if new_cost<dist[v]:
                dist[v]=new_cost
                heapq.heappush(pq,(new_cost,v))

    print(-1)

solve()