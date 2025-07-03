
T=int(input())


for far in range(T):
    N=int(input())
    arr1=(input().split())
    for han in range(len(arr1) - 1):
        if int(arr1[han]) > int(arr1[han + 1]):
            print("NO")
            break
    else:
        print("YES")
