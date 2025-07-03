T=int(input())
for far in range(T):
      
      div= input().split()
      if div[2]=="+":
         print(float(div[1])+float(div[3]))
      elif div[2]=="-":
         print(float(div[1])-float(div[3]))
      elif div[2]=="*":
         print(float(div[1])*float(div[3]))
      elif div[2]=="/":
         
         print(float(div[1])/float(div[3]))
      