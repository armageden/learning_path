# Home Task 4: Username Generator
def username_generator(first_name, last_name, student_id, middle_name=None):
    part_1=first_name[0]+chr(ord(first_name[1])-32)+chr(ord(first_name[2])-32)
    part_2=""
    if middle_name:
        part_2=middle_name
    pre_part_3=last_name
    part_3=chr(ord(pre_part_3[0])+32)+chr(ord(pre_part_3[1])+32)+chr(ord(pre_part_3[2])+32)
    part_4=str(student_id)[-4:]
    user_name=part_1+part_2+part_3+"_"+part_4
    return user_name
    
first_name, middle_name, last_name, student_id= input ("First Name:"), input("Middle Name:"), input ("Last Name:"), int (input ("Student ID:"))
print(username_generator (first_name, last_name, student_id))
print(username_generator(first_name, last_name, student_id, middle_name))