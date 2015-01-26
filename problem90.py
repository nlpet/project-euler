from __future__ import division
from itertools import combinations


def found_all_sqs(d1,d2):
  return all(x in c1 and y in c2 or x in c2 and y in c1 for x, y in sqs)
  

sqs = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(4,6),(8,1)]
combs = list(combinations([0,1,2,3,4,5,6,7,8,6],6))

t = 0
for i,c1 in enumerate(combs):
  for c2 in combs[:i]:
    if found_all_sqs(c1,c2): t += 1
    
print t