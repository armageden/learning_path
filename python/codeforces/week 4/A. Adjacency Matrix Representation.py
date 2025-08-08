n,m=map(int,input().split())
ad_mat=[[0]*n for _ in range(n)]
for _ in range(m):
    u,v,w=map(int,input().split())
    ad_mat[u-1][v-1]=w
for i in range(n):
    print(*ad_mat[i])  