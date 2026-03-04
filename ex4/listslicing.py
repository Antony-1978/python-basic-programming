list1=[10,20,30,40,50,60,70,80,90,100]
start=int(input("enter start index:"))
end=int(input("enter end index:"))
list2=list1[start:end]

odd=[x for x in list1 if x%2!=0]
even=[y for y in list1 if y%2==0]

result=even+odd

print("Original List:",list1)
print("Sliced List:",list2)
print("Final List :",result)
