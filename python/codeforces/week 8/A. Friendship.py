import sys
sys.setrecursionlimit(300005)

def find(i,p):
    #valo lage na re
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
    print(s[ra]) #r akorbo na

def solve():
    try:
        line=sys.stdin.readline()
        if not line:
            return
        n,k=map(int,line.split())
        p=list(range(n+1))
        s=[1]*(n+1)
        #ami ki parbo re vai?
        for _ in range(k):
            a,b=map(int,sys.stdin.readline().split())
            union(a,b,p,s)
    except (IOError,ValueError):
        pass

solve()