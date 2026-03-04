x=[]
y=int(input("Enter how many numbers you want: "))
for i in range(y):
   z=int(input("Enter a number: "))
   x.append(z)
x=[z + 5 for z in x]
print("Updated list:", x)
print("Maximum:", max(x))
print("Minimum:", min(x))
