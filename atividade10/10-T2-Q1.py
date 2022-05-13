nx = int(input().strip())
cont = 0
acm = 0

if nx == 0:
  print('0')
  exit()

while nx != 0:
  acm+=nx
  nx = int(input().strip())
  cont+=1


print(acm)