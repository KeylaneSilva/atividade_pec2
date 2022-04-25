maior = None
menor = None
for i in range(5):
   atual = int(input())
   if i==0 or atual>maior:
    maior = atual
   if i==0 or atual<menor:
    menor = atual

print(maior)
print(menor)