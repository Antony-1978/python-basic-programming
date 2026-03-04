n=str(input("Enter string:"))
if(len(n)<3):
   print("output string:",n)
else:
   d='ing'
   if d not in n:
      x=n+d
      print("output string:",x)
   if d in n:
      y=n+'ly'
      print("output string:",y)
