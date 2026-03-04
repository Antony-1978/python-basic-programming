n=str(input("enter string:"))
x,y,z=0,0,0
for c in n:
   if c.isdigit():
      x+=1
   elif c.isalpha():
      y+=1
   elif c.isspace():
      z+=1

print("no of digits:",x)
print("no of alphabets:",y)
print("no of spaces:",z)
