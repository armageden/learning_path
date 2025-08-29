import sys
import heapq

def solve():
    n, m, s, d = map(int, sys.stdin.readline().split())
    u_list = list(map(int, sys.stdin.readline().split()))
    v_list = list(map(int, sys.stdin.readline().split()))
    w_list = list(map(int, sys.stdin.readline().split()))
    
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[u_list[i]].append((v_list[i], w_list[i]))
    
    dist = [float('inf')] * (n + 1)
    parent = [0] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        w, u = heapq.heappop(pq)
        
        if w > dist[u]:
            continue
        
        if u == d:
            break
        
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    if dist[d] == float('inf'):
        print(-1)
        return
    
    print(dist[d])
    
    path = []
    curr = d
    while curr != 0:
        path.append(curr)
        curr = parent[curr]
    
    path.reverse()
    print(*path)

solve()