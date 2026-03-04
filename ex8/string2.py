def check(S):
   u=0
   l=0
   for c in S:
      if c.isupper():
         u+=1
      elif c.islower():
         l+=1
   print("Upper:",u)
   print("Lower:",l)

s=input("Enter the string: ")
check(s)
