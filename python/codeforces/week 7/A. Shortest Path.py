import sys
input = sys.stdin.readline
import heapq
N,M,S,D=map(int,input().split())
u=map(int,input().split())
v=map(int,input().split()) 
w=map(int,input().split())
adj=[[] for _ in range(N+1)]
for i in range(M):
    adj[u[i]].append((v[i],w[i]))
dist=[float('inf')]*(N+1)
par=[0]*(N+1)
dist[S]=0
pq=[(0,S)]
while pq:
    d,node=heapq.heappop(pq)
    if d>dist[node]:
        continue
    for child,weight in adj[node]:
        if dist[child]>d+weight:
            dist[child]=d+weight
            par[child]=node
            heapq.heappush(pq,(dist[child],child))