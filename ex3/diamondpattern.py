x=int(input( "enter the size "))
for i in range(1,x+1):
   print(" "*(x-i),"* "*i)
for j in range(x-1,0,-1):
   print(" "*(x-j),"* "*j)
