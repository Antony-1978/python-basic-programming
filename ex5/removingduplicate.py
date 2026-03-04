tup1=(1,2,3,2,4,3,5,6,5)
list1=[]
for x in tup1:
   if x not in list1:
      list1.append(x)
print(tup1)
tuple2=tuple(list1)
print("Without duplicates:",tuple2)
