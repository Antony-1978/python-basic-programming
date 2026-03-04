x=int(input("enter no.of elements in dictionary1:"))
dict1={}
for i in range(x):
   k=int(input("enter key:"))
   v=int(input("enter value:"))
   dict1[k]=v

y=int(input("enter no.of elements in dictionary2:"))
dict2={}
for i in range(y):
   k=int(input("enter key:"))
   v=int(input("enter value:"))
   dict2[k]=v

dict1.update(dict2)
print(dict1)

n=int(input("enter the key:"))
if n in dict1:
   print("key is present")
else:
   print("key is not present")
