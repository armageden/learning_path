import heapq
import math
N,M,S,D=map(int,input().split())
w=[0]+list(map(int,input().split()))
adj=[[] for i in range(N+1)]
for i in range(M):
    u,v=map(int,input().split())
    adj[u].append(v)
dis=[math.inf]*(N+1)
dis[S]=w[S]
q=[(dis[S],S)]
while q:
    d,node=heapq.heappop(q) #(cost,node)
    if d!=dis[node]:
        continue #skip if not optimal 
    for nei in adj[node]:
        curr_cost=d+w[nei]
        if curr_cost<dis[nei]:
            dis[nei]=curr_cost
            heapq.heappush(q,(curr_cost,nei))
if dis[D]==math.inf:
    print(-1)
else:
    print(dis[D])