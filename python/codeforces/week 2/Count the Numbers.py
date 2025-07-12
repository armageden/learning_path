import sys

def find_left_boundary(array, val):
    low, high = 0, len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] < val:
            low = mid + 1
        else:
            high = mid
    return low
#this damn sys making me go ....
def find_right_boundary(array, val):
    low, high = 0, len(array)
    while low < high:
        mid = (low + high) // 2
        if array[mid] <= val:
            low = mid + 1
        else:
            high = mid
    return low




#test 3,5 failed ???
n_val, q_val = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
#ahhhhhhhhhhhhhh
for i in range(q_val):
    x, y = map(int, sys.stdin.readline().split())
    
    start = find_left_boundary(nums, x)
    end = find_right_boundary(nums, y)
    #print(start, end)  
    # if start == end:
    #     print(0)
    # else:
    print(end - start)