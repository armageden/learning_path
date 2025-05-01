#home task 2 lab 3
num1=int(input())
num2=0
length=(len(str(num1)))-1
while num1!=0 :
    
    num2=num1//(10**length)
    num1=num1%(10**length)
    length-=1
    if num2//10==num1:
     print(num2,end="")
    else:
     print(num2,end=", ")  
    