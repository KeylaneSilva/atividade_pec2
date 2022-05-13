nx = int(input().strip())
if nx == 0:
  exit()

cont = 0
acm = 0
media = 0
maior = 0
menor = nx

while nx != 0:
  nx = int(input().strip())
  if nx == 0:
    break
  if nx >= maior:
    maior = nx
  if nx <= menor:
    menor = nx
  cont+=1

print(maior)
print(menor)
