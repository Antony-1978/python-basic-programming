x=int(input("enter x value:"))
y=int(input("enter y value:"))
if(x>y):
   z=x
else:
   z=y
while (True):
   if(z%x==0 and z%y==0):
      l=z
      break
   else:
      z=z+1
print("LCM: ",l)
