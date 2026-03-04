print("##....Enter 'end' to stop....##")
mytuple=()
while True:
   key=input("Enter value:")
   if key=="end":
      break
   mytuple=mytuple+(key,)
print("my tuple:",mytuple)
