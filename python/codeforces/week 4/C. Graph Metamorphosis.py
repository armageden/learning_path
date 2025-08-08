n = int(input())
adj_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    k = data[0] 
    for v in data[1:]:
        adj_matrix[i][v] = 1

for row in adj_matrix:
    print(*row)
