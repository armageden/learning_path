T=int(input())
for far in range(T):
    k,x=map(int,input().split())
    ign_c=(k-1)//(x-1) 
    final=k+ign_c
    print(final)
#will it work? seems too easy to be true........nope not that easy..
#well well it is