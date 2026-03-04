n=int(input("enter a value:"))
x=0
y=1
count=2
s=[0,1]
while count<n:
   z=x+y
   s.append(z)
   x=y
   y=z
   count+=1
print(s)
