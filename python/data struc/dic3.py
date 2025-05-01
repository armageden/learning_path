# Home Task 2: 007
def is_james_bond(int_list):
    num=7

    for i in range(len(int_list)):
        if int_list[i]==7:
            lim=i
            count=0
            for j in range(lim):
                
                if int_list[j]==0:
                    count+=1
            if count>1:
                return True
            else:
                return False

print(is_james_bond([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(is_james_bond([1, 7, 2, 0, 4, 5, 0]))  # Output: False
print(is_james_bond([1, 0, 2, 0, 4, 7, 5]))  # Output: True
