M=10**9+7
def mul(A,B):
    C=[[0,0],[0,0]]
    C[0][0]=(A[0][0]*B[0][0]+A[0][1]*B[1][0])%M
    C[0][1]=(A[0][0]*B[0][1]+A[0][1]*B[1][1])%M
    C[1][0]=(A[1][0]*B[0][0]+A[1][1]*B[1][0])%M
    C[1][1]=(A[1][0]*B[0][1]+A[1][1]*B[1][1])%M
    return C
def mpow(A,x):
    res=[[1,0],[0,1]]
    b=A
    while x>0:
        if x%2==1:
            res=mul(res,b)
        b=mul(b,b)
        x//=2
    return res
T=int(input())
for _ in range(T):
    a11,a12,a21,a22=map(int,input().split())
    x=int(input())
    A=[[a11,a12],[a21,a22]]
    ans=mpow(A,x)
    print(ans[0][0],ans[0][1])
    print(ans[1][0],ans[1][1])