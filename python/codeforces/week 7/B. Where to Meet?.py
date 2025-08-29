import sys
import heapq

def dijkstra(n, start, adj):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def solve():
    n, m, s, t = map(int, sys.stdin.readline().split())
    
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        rev_adj[v].append((u, w))
    
    dist_a = dijkstra(n, s, adj)
    dist_b = dijkstra(n, t, rev_adj)
    
    min_time = float('inf')
    meet_node = -1
    
    for i in range(1, n + 1):
        if dist_a[i] != float('inf') and dist_b[i] != float('inf'):
            meet_time = max(dist_a[i], dist_b[i])
            if meet_time < min_time:
                min_time = meet_time
                meet_node = i
    
    if meet_node == -1:
        print(-1)
    else:
        print(min_time, meet_node)

solve()