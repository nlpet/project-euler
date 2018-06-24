from __future__ import division
from math import log

f = open("p099_base_exp.txt","r")

largest_so_far = (0,0)

for i,line in enumerate(f.readlines()):
  b,e = line.strip().split(",")
  result = float(e) * log(float(b))
  if result > largest_so_far[1]: largest_so_far = (i+1,result,b,e)
  
print "Largest number is on line #%s" % largest_so_far[0]