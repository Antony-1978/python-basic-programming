n=int(input("enter value:"))
x=n
flag=0
for i in range(2,n):
   if((x%i)==0):
      flag=1
if flag==1:
   print("Not a prime number")
else:
   print("prime number")
