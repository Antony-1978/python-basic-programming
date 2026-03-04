n=int(input("enter the range:"))
s=set()
for i in range(n):
   e=int(input("enter element:"))
   s.add(e)

print(s)
print("length of set:",len(s))

def search(i):
   x=int(input("element to be searched:"))
   if x in i:
      print("The element ",x," is exsist in the set")
   else:
      print("The element ",x," is not present in the list")

search(s)
