from math import sqrt

l = 2
count = 0
target = 10**6

while count < target:
  l += 1
  for wh in range(3,2*l+1):
    sqroot = sqrt(wh * wh + l * l)
    if sqroot == int(sqroot):
      count += wh / 2 if wh <= l else 1 + (l - (wh+1)/2)
      
print l      