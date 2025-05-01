list1=input()
temp=""
for i in range(len(list1)+1):
    temp=list1[i]
    list1[i]=list[-(i+1)]
    list[-(i+1)]=temp      
print(list1)