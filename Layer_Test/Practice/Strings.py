name = "Veena Katiyar"

i = 0
k= 0
j = len(name)

while(k<=j):
  start = k
  q = k
  while(q <= j):
   print(name[start:q])
   q = q+1

  k = k+1