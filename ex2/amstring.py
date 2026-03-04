x=int(input("enter a value:"))
y=x
n=0
while(y!=0):
   z=y%10
   n=n+(z**3)
   y=y/10
if (x==n):
   print("the number is amstrong number")
else:
   print("not amstrong number")
