# n=int(input())
# a=list(map(int,input().split()))
# count=0
# for i in range(n):
#     for j in range(i+1,n):
#         if a[i]>a[j]:
#             count+=1

#     for k in range(n-i-1):
#         if a[k]>a[k+1]:
#             a[k], a[k+1]=a[k+1], a[k]
    
        
# print(count)
# print(*a)
# brute-force approch
def merge(left, right):
    merged = []
    i = j = 0
    count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, count
def mergeSort(arr):
    if len(arr) < 2:
        return arr, 0

    mid = len(arr)//2
    left, left_count = mergeSort(arr[:mid])
    
    
    right, right_count = mergeSort(arr[mid:])
    mer_arr, merge_count = merge(left, right)
    final_count = left_count + right_count + merge_count
    return mer_arr, final_count
n = int(input())
a = list(map(int, input().split()))
final_a, count = mergeSort(a)
print(count)
print(*final_a)