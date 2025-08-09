n=int(input())
x,y=map(int,input().split())
m=[]
for dx in(-1,0,1):
    for dy in(-1,0,1):
        if dx==0 and dy==0:
            continue
        nx=x+dx
        ny=y+dy
        if 1<=nx<=n and 1<=ny<=n:
            m.append((nx,ny))
m.sort()
print(len(m))
for a,b in m:
    print(a,b)

