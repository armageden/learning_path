import sys
input = sys.stdin.readline


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    adj[i].append(j)
    adj[j].append(i)

q = [1]
vis = [False] * (n + 1)
vis[1] = True
res = []

while q:
    u = q.pop(0)
    res.append(u)
    for v in adj[u]:
        if not vis[v]:
            vis[v] = True
            q.append(v)
            
print(*res)

