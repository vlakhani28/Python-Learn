def displayInventory(inventory) :
 c = 0
 for items in inventory :
  print(inventory[items] ," " ,items)
  c = int(inventory[items])+c;
 print("Total number of items" , c)


dict = {}
while True:
 key = input("Enter Key")
 dict[key] = input("Enter value")
 print("Enter N to exit")
 if input()=="N":
  break

displayInventory(dict)
