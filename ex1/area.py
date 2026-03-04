n=int(input("enter no of input:"))
if(n==2):
   l=int(input("enter l:"))
   b=int(input("enter b:"))
   if ( l<=0 or b<=0):
      print(" invalied inputs")
   else:
      area=0.5*l*b
      print("AREA=",area)
elif(n==3):
   x=int(input("enter value1:"))
   y=int(input("enter value2:"))
   z=int(input("enter value3:"))
   if (x<=0 or y<=0 or z<=0):
      print(" invalied inputs")
   else:
      s=(x+y+z)/2
      area=(s*(s-x)*(s-y)*(s-z))**0.5
      print("AREA=",area)
