n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
diff = [0] * (n + 1)
for i in range(m):
    diff[u[i]] -= 1
    diff[v[i]] += 1
print(*diff[1:])
