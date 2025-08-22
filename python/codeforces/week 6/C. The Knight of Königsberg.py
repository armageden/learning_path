import sys
from collections import deque
input=sys.stdin.readline
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
q1=deque([(x1,y1)])
d1=[[-1]*n for _ in range(n)]
d1[x1][y1]=0
q2=deque([(x2,y2)])
d2=[[-1]*n for _ in range(n)]
d2[x2][y2]=0
while q1 and q2:
    if len(q1)<=len(q2):
        x,y=q1.popleft()
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if d1[nx][ny]==-1:
                    d1[nx][ny]=d1[x][y]+1
                    if d2[nx][ny]!=-1:
                        print(d1[nx][ny]+d2[nx][ny])
                        exit()
                    q1.append((nx,ny))
    else:
        x,y=q2.popleft()
        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if d2[nx][ny]==-1:
                    d2[nx][ny]=d2[x][y]+1
                    if d1[nx][ny]!=-1:
                        print(d1[nx][ny]+d2[nx][ny])
                        exit()
                    q2.append((nx,ny))
print(-1)