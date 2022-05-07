cont = 1
primeiro = 0
maior = 0
while cont <= 100:
  num = int(input().strip())
  if num > maior:
    maior = num

  cont+=1

print(maior)