# Home Task 3: Section Assigning
def assign_students_to_sections(sec_str,*names):
    sec_dic={}
    for i in sec_str:
        sec_dic[i]=[]
    
    for name in names:
        num=0
        for k in name:
               num+=ord(k)
        ind_sec=num%len(sec_str)
        i=sec_str[ind_sec]
        sec_dic[i].append(name)
        
    return sec_dic

print(assign_students_to_sections ('ABCDE', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'))
