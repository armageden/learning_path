import sys
input = sys.stdin.readline
sys.setrecursionlimit(200005)
def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    vis = [0] * (n + 1)
    def dfs(u):
        vis[u] = 1
        for v in adj[u]:
            if vis[v] == 1:
                return True
            if vis[v] == 0:
                if dfs(v):
                    return True
        vis[u] = 2
        return False
    cycle = False
    for i in range(1, n + 1):
        if vis[i] == 0:
            if dfs(i):
                cycle = True
                break
    if cycle:
        print("YES")
    else:
        print("NO")
solve()