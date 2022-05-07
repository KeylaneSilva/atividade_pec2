prestacao = 1
valor = float(input().strip())
while prestacao <= 24:
  print(str(prestacao)+'x de R$',('{:.2f}'.format(valor/prestacao)))
  prestacao+=1