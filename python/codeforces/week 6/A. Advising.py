import sys
from collections import deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        indegree[b] += 1
    
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i) 
    
    res = []
    while q:
        curr = q.popleft()
        res.append(curr)
        
        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    
    if len(res) == n:
        print(*res)
    else:
        print(-1)

solve()