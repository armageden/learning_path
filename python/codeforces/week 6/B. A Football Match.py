import sys
from collections import deque
    
def solve():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    ans = 0
    
    for i in range(1, n + 1):
        if color[i] == 0:
            q = deque([i])
            color[i] = 1
            c1, c2 = 0, 0
            is_bipartite = True
            
            while q:
                u = q.popleft()
                if color[u] == 1:
                    c1 += 1
                else:
                    c2 += 1
                
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
            
            if is_bipartite:
                ans += max(c1, c2)
            else:
                print(0)
                return
    
    print(ans)
    
solve()