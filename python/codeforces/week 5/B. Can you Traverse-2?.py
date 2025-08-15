import sys
sys.setrecursionlimit(200005)
def solve():
    n, m = map(int, input().split())
    ul = list(map(int, input().split()))
    vl = list(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = ul[i], vl[i]
        adj[u].append(v)
        adj[v].append(u)
    vis = [False] * (n + 1)
    res = []
    def dfs(u):
        vis[u] = True
        res.append(u)
        for v in adj[u]:
            if not vis[v]:
                dfs(v)
    dfs(1)
    print(*res)
solve()