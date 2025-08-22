from collections import deque
n=int(input())
x1,y1,x2,y2=map(int,input().split())
x1-=1
y1-=1
x2-=1
y2-=1
if x1==x2 and y1==y2:
    print(0)
    exit()
moves=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
v=[[False]*n for _ in range(n)]
q=deque([(x1,y1,0)])
v[x1][y1]=True
while q:
    x,y,s=q.popleft()
    for dx,dy in moves:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and not v[nx][ny]:
            if nx==x2 and ny==y2:
                print(s+1)
                exit()
            v[nx][ny]=True
            q.append((nx,ny,s+1))
print(-1)