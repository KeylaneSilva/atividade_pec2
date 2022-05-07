cont = 1
impar = 0
par = 0
while cont <=100:
  num = int(input().strip())
  if num%2==0:
    par+=1
  else:
    impar+=1
  cont+=1

print(par)
print(impar)
