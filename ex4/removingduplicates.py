x=[10,20,50,60,70,20,50,10,56,77]
y=[]
for z in x:
   if z not in y:
      y.append(z)
z=list(set(x))
print("Original list:", x)
print("Without duplicates (order preserved):", y)
print("Without duplicates (order not preserved):", z)
