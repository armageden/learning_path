import sys
input = sys.stdin.readline
sys.setrecursionlimit(200005)
def solve():
    n, r = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    size = [0] * (n + 1)
    def dfs(u, p):
        s = 1
        for v in adj[u]:
            if v != p:
                s += dfs(v, u)
        size[u] = s
        return s
    dfs(r, 0)
    q_count = int(input())
    for _ in range(q_count):
        x = int(input())
        print(size[x])
solve()