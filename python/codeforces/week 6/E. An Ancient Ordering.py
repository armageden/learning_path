import sys
from collections import defaultdict
import heapq
n=int(sys.stdin.readline())
ws=[sys.stdin.readline().strip() for _ in range(n)]
a=defaultdict(set)
i_d=defaultdict(int)
cs=set()
for w in ws:
    for c in w:
        cs.add(c)
for i in range(n-1):
    w1,w2=ws[i],ws[i+1]
    if len(w1)>len(w2) and w1.startswith(w2):
        print(-1)
        exit()
    for j in range(min(len(w1),len(w2))):
        if w1[j]!=w2[j]:
            u,v=w1[j],w2[j]
            if v not in a[u]:
                a[u].add(v)
                i_d[v]+=1
            break
pq=[]
for c in cs:
    if i_d[c]==0:
        heapq.heappush(pq,c)
res=[]
while pq:
    u=heapq.heappop(pq)
    res.append(u)
    for v in a[u]:
        i_d[v]-=1
        if i_d[v]==0:
            heapq.heappush(pq,v)
if len(res)==len(cs):
    print("".join(res))
else:
    print(-1)