import sys
sys.setrecursionlimit(200005)

def find(p,i):
    root=i
    while root!=p[root]:
        root=p[root]
    while i!=root:
        next_i,p[i]=p[i],root
        i=next_i
    return root

def union(p,r,a,b):
    ra=find(p,a)
    rb=find(p,b)
    if ra==rb:return False
    if r[ra]<r[rb]:ra,rb=rb,ra
    p[rb]=ra
    if r[ra]==r[rb]:r[ra]+=1
    return True

def solve():
    try:
        line=sys.stdin.readline()
        if not line:return
        n,m=map(int,line.split())
        edges=[]
        for i in range(m):
            u,v,w=map(int,sys.stdin.readline().split())
            edges.append((w,u-1,v-1,i))
        
        edges.sort()
        p=list(range(n))
        r=[0]*n
        mst_e=[]
        cost=0
        count=0
        # bismillah, cholo shuru kori
        for w,u,v,idx in edges:
            if union(p,r,u,v):
                mst_e.append(idx)
                cost+=w
                count+=1
        
        if count!=n-1:
            print(-1)
            return

        s_best=float('inf')
        for ex_idx in mst_e:
            p1=list(range(n))
            r1=[0]*n
            w1=0
            c1=0
            for i in mst_e:
                if i!=ex_idx:
                    w,u,v,_=edges[i]
                    if union(p1,r1,u,v):
                        w1+=w
                        c1+=1
            # ei part ta ektu pechano
            for i in range(m):
                if i not in mst_e:
                    w,u,v,_=edges[i]
                    if union(p1,r1,u,v):
                        w1+=w
                        c1+=1
                        if c1==n-1 and w1>cost:
                            s_best=min(s_best,w1)
                        break
        
        print(s_best if s_best!=float('inf') else -1) # eibar hoile hoy
    except(IOError,ValueError):
        pass

solve()