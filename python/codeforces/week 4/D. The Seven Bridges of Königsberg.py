n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

degree = [0] * (n + 1)

for a, b in zip(u, v):
    if a == b:  # self loop
        degree[a] += 2
    else:
        degree[a] += 1
        degree[b] += 1

odd_count = sum(1 for d in degree if d % 2 == 1)

if odd_count == 0 or odd_count == 2:
    print("YES")
else:
    print("NO")
