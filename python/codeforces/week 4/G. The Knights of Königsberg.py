n,m,k=map(int,input().split())
s=set()
d=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
for _ in range(k):
    x,y=map(int,input().split())
    for dx,dy in d:
        if (x+dx,y+dy) in s:
            print("YES")
            exit()
    s.add((x,y))
print("NO")
