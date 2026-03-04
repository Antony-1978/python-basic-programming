a=[10,20,30,40]
b=[5,10,15,20,25]
print("list a:",a)
print("list b:",b)
if not a and not b:
    print("Both lists are empty")
elif not a or not b:
    print("One of the lists is empty")
else:
    print("Both lists are not empty")

def common(list1,list2):
   for item in list1:
      if item in list2:
         return True
   return False

print("Common element:", common(a,b))

def delete(list3,list4,e):
   if e in list3:
      list3.remove(e)
   if e in list4:
      list4.remove(e)

ele=int(input("Enter element to remove from list a: "))
delete(a,b,ele)
print("removed list a:",a)
print("removed list b:",b)

newlist=[]
for i in a:
   for j in b:
      if i+j>40:
         newlist.append([i,j])
print("New list:", newlist)
