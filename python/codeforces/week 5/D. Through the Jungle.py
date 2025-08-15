import sys
input = sys.stdin.readline
def bfs(start, n, adj):
    dist = [-1] * (n + 1)
    par = [0] * (n + 1)
    q = [start]
    dist[start] = 0
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                par[v] = u
                q.append(v)
    return dist, par
def solve():
    n, m, s, d, k = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    dist_s, par_s = bfs(s, n, adj)
    if dist_s[k] == -1:
        print(-1)
        return
    dist_k, par_k = bfs(k, n, adj)
    if dist_k[d] == -1:
        print(-1)
        return
    print(dist_s[k] + dist_k[d])
    path1 = []
    curr = k
    while curr:
        path1.append(curr)
        curr = par_s[curr]
    path1.reverse()
    path2 = []
    curr = d
    while curr:
        path2.append(curr)
        curr = par_k[curr]
    path2.reverse()
    res = path1 + path2[1:]
    print(*res)
solve()