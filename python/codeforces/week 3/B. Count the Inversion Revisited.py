# n=int(input())
# a=list(map(int,input().split()))
# count=0
# for i in range(n):
#     for j in range(i+1,n):
#         if a[i]>a[j]**2:
#             count+=1
# print(count)
# brute force approach


def m(l, r):
    r2 = [x * x for x in r]
    r2.sort()
    from bisect import bisect_left as b

    c = sum(b(r2, x) for x in l)
    i = j = 0
    a = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            a.append(l[i])
            i += 1
        else:
            a.append(r[j])
            j += 1
    a += l[i:] + r[j:]
    return a, c


def s(a):
    if len(a) <= 1:
        return a, 0
    m1, v1 = s(a[: len(a) // 2])
    m2, v2 = s(a[len(a) // 2 :])
    m3, v3 = m(m1, m2)
    return m3, v1 + v2 + v3


n = int(input())
a = list(map(int, input().split()))
print(s(a)[1])
