n, m = map(int, input().split())

u_nodes = list(map(int, input().split()))
v_nodes = list(map(int, input().split()))
w_values = list(map(int, input().split()))

adj_list = [[] for _ in range(n + 1)]

for i in range(m):
    u = u_nodes[i]
    v = v_nodes[i]
    w = w_values[i]
    adj_list[u].append((v, w))

for i in range(1, n + 1):
    print(f"{i}:", end="")
    for v, w in adj_list[i]:
        print(f" ({v},{w})", end="")
    print()