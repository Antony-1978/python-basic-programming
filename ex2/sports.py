t=input("enter the state of temparature:")
h=input("enter the state of humidity:")
if(t=="warm" or t=="cold" and h=="humid" or h=="dry"):
   if(t=="warm" and h=="dry"):
      print("you can play basket ball")
   elif (t=="warm" and h=="humid"):
      print("you can play tennis")
   elif (t=="cold" and h=="dry"):
      print("you can play cricket")
   elif (t=="cold" and h=="humid"):
      print("you can swim")
else:
   print("invalid inputs")
