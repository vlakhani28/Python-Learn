Pass = {}
j = 0
un = ""
while True :
 print("Enter Username : ")
 un = input()
 print("Enter Password : ")
 Pass[un] = input()
 j = j+1
 print("To add more type Y else N")
 i = input()
 if i== "N":
  break;

print(Pass)
print("Enter account name")
acc = input()
if acc in Pass :
 print(Pass[acc])

else :
 print("Not Found")
