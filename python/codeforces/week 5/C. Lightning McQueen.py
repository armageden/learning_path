import sys
input = sys.stdin.readline
n, m, s, d = map(int, input().split())
adj = [[] for _ in range(n + 1)]
if m > 0:
    ul = list(map(int, input().split()))
    vl = list(map(int, input().split()))
    for i in range(m):
        adj[ul[i]].append(vl[i])
        adj[vl[i]].append(ul[i])
for i in range(n + 1):
    adj[i].sort()
dist = [-1] * (n + 1)
par = [0] * (n + 1)
q = [s]
dist[s] = 0
head = 0
while head < len(q):
    u = q[head]
    head += 1
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            par[v] = u
            q.append(v)
if dist[d] == -1:
    print(-1)
else:
    print(dist[d])
    path = []
    curr = d
    while curr:
        path.append(curr)
        curr = par[curr]
    print(*path[::-1])