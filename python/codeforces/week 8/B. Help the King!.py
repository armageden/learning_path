import sys
sys.setrecursionlimit(200005)

def find(i,p):
    if p[i]==i:
        return i
    p[i]=find(p[i],p)
    return p[i]

def union(a,b,p,s):
    ra=find(a,p)
    rb=find(b,p)
    if ra!=rb:
        if s[ra]<s[rb]:
            ra,rb=rb,ra
        p[rb]=ra
        s[ra]+=s[rb]
        return True
    return False

def solve():
    try:
        #ami ki parbo re vai?
        line=sys.stdin.readline()
        if not line:return
        n,m=map(int,line.split())
        edges=[]
        for _ in range(m):
            u,v,w=map(int,sys.stdin.readline().split())
            edges.append((w,u,v))
        
        edges.sort()
        
        p=list(range(n+1))
        s=[1]*(n+1)
        
        cost=0
        #valo lage na re
        for w,u,v in edges:
            if union(u,v,p,s):
                cost+=w
        
        print(cost)
    except(IOError,ValueError):
        pass

solve()