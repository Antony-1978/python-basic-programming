def diction(i):
    dict1={}
    for c in i:
        if c in dict1:
            dict1[c]+=1
        else:
            dict1[c]=1
    return dict1

s=input("Enter string:")
result=diction(s)
print(result)
