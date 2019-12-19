def convert(list):
 print(type(list))
 return ",".join(list)

l=[]
while True:
 print("Enter item")
 l.append(input())
 print("Enter N to exit")
 if(input() == "N"):
  break
print(convert(l))
