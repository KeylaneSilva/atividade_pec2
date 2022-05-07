cont = 1
acm = 0
while cont <=100:
  num = int(input().strip())
  acm+=num
  cont+=1

media = acm/100
print('{:.2f}'.format(media))

