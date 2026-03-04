def sortdict(n,d):
    a=int(input("Enter the element: "))
    d[n+1]=a
    print("Before sort:", d)
    d=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    print("Sorted (Descending):",d)

c={2:22,1:11,3:33,5:55,4:44}
print("Actual Dictionary:",c)
a=dict(sorted(c.items(), key=lambda x: x[1]))
print("Sorted (Ascending):",a)
n=len(c)
sortdict(n, c)
