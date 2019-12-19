"""
f1 = open("abc.txt")
f = f1.read()
count = {}
t = f.split();
for i in t:
 count.setdefault(i,0);
 count[i]+=1;

j = 0
count = sorted(count.items(),key = lambda abc:(abc[1],abc[0]),reverse = True)
while j!=10:
 print(count[j]);
 j = j+1
"""
from collections import defaultdict
counts = defaultdict(int)
with open("abc.txt") as feed:
 for current in feed.readlines():
  for token in current.split():
   counts[token.lower()] += 1

counts = sorted(counts.items(),key = lambda abc:(abc[1],abc[0]),reverse = True)[:10]
print (counts)
