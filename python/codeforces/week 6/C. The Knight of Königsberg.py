from collections import deque
n = int(input())
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
moves = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)]
seen = {(x1,y1)}
q = deque([(x1,y1,0)])
while q:
    x, y, steps = q.popleft()
    if x == x2 and y == y2:
        print(steps)
        exit()
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and (nx,ny) not in seen:
            seen.add((nx,ny))
            q.append((nx,ny,steps+1))
print(-1)