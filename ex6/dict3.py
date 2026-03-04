def summ(x):
   add=0
   for j in d:
      add=add+x[j]
   print("addition:",add)

n=int(input("enter range value:"))
d={}
for i in range(1,n+1):
   d[i]=i*i

print(d)
summ(d)
