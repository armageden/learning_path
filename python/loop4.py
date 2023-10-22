# home task 4 lab3
quantity=int(input("Enter quantity: "))
max=0
min=0
total=0
avg=0
for i in range(quantity):
    num=int(input())
    
    if num > max:
        max=num
    if num<min:
        min=num
    total+=num
avg=total/quantity
print("Maximum=",max)
print("Minimum=",min)
print("Avarage is=",avg)
