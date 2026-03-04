a=input("Enter the binary inputs: ")
list=a.split(',')
mylist=[]
print(list)
for x in list:
   if int(x,2)%5==0:
      mylist.append(x)
   else:
      continue
print(mylist)
