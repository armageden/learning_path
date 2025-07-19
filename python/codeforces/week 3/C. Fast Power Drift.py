# a,b=map(int,input().split())
# print(pow(a,b)%107)

# brute force

a,b=map(int,input().split())
fin=1
while b>0:
    if b%2==1:
        fin=(fin*a)%107
    a=(a*a)%107
    b//=2
print(fin)