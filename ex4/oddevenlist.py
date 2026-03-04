n=int(input("Enter number of elements: "))
list1=[]
for i in range(n):
   z=int(input("Enter element: "))
   list1.append(z)

evenlist=[]
for value in list1:
   if value%2==0:
      evenlist.append(value)

even=[]
odd=[]
for value in list1:
   if value%2==0:
      even.append(value)
   else:
      odd.append(value)

list2=even+odd

print("Input List:",list1)
print("Even List:",evenlist)
print("Third List:",list2)
