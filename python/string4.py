#home task 4 lab 4
str1=input("Enter a string: ")
str2=""
capital=True
for i in str1:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        if capital:
            if 'a'<= i<='z':
                str2=str2+chr(ord(i)-ord('a')+ord('A'))
            else:
                str2+=i 
        else:
            if 'A'<=i<='Z':
                str2=str2+chr(ord(i)-ord('A')+ord('a'))
            else:
                str2=str2+i
        capital=not capital
    else:
        str2+=i
print(str2)