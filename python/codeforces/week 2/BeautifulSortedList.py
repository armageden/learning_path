import sys

def solve():



    n = int(sys.stdin.readline())
    listA = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    listB = list(map(int, sys.stdin.readline().split()))

    ptr1 = 0
    ptr2 = 0


    merged_list = []

    while ptr1 < n and ptr2 < m:
            if listA[ptr1] < listB[ptr2]:
                merged_list.append(listA[ptr1])
                ptr1+=1
            else:
                merged_list.append(listB[ptr2])
                ptr2+= 1

    while ptr1<n:
        merged_list.append(listA[ptr1])
        ptr1 += 1
    
    while ptr2 < m:
        merged_list.append(listB[ptr2])
        ptr2 += 1
#can I really make it this simple?
    print(*merged_list)

solve()