import sys
input = sys.stdin.readline
def solve():
    r, h = map(int, input().split())
    grid = [input().strip() for _ in range(r)]
    vis = [[False for _ in range(h)] for _ in range(r)]
    max_d = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(r):
        for j in range(h):
            if grid[i][j] != '#' and not vis[i][j]:
                curr_d = 0
                q = [(i, j)]
                vis[i][j] = True
                head = 0
                while head < len(q):
                    row, col = q[head]
                    head += 1
                    if grid[row][col] == 'D':
                        curr_d += 1
                    for k in range(4):
                        nr, nc = row + dr[k], col + dc[k]
                        if 0 <= nr < r and 0 <= nc < h and not vis[nr][nc] and grid[nr][nc] != '#':
                            vis[nr][nc] = True
                            q.append((nr, nc))
                max_d = max(max_d, curr_d)
    print(max_d)
solve()