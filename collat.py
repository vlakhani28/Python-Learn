def collatz(number):
 if number%2==0 :
  return number//2 
 else :
  return (3*number)+1

n = int(input("Enter Number : "))
while n>=1
 print(n)
 n = collatz(n) 
