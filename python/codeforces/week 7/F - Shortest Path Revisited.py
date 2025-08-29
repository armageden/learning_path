import heapq
import sys

def solve():
    n, m, s, d = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    dist1 = [float('inf')] * (n + 1)
    dist2 = [float('inf')] * (n + 1)
    
    dist1[s] = 0
    pq = [(0, s)]
    
    while pq:
        cost, u = heapq.heappop(pq)
        
        if cost > dist2[u]:
            continue
            
        for v, w in adj[u]:
            new_cost = cost + w
            
            if new_cost < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = new_cost
                heapq.heappush(pq, (dist1[v], v))
                heapq.heappush(pq, (dist2[v], v))
            elif new_cost > dist1[v] and new_cost < dist2[v]:
                dist2[v] = new_cost
                heapq.heappush(pq, (dist2[v], v))
                
    if dist2[d] == float('inf'):
        print(-1)
    else:
        print(dist2[d])

solve()