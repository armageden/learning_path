
# home task 5 lab3
num=int(input())
max=0
min=0
avg=0
sum=0
for i in range(1,num+1):
  inp=int(input())
  sum+=inp
  avg=sum/num
  if inp>max:
    max=inp
  if inp<min:
    min=inp
print("Maximum",max)
print("Minimum",min)
print("Average is",avg)

 #### or #####
# quantity=int(input("Enter quantity: "))
# max=0
# min=0
# total=0
# avg=0
# for i in range(quantity):
#     num=int(input())
    
#     if num > max:
#         max=num
#     if num<min:
#         min=num
#     total+=num
# avg=total/quantity
# print("Maximum=",max)
# print("Minimum=",min)
# print("Avarage is=",avg)