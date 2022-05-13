depositoInicial = float(input().strip())
taxaJuros = float(input().strip())
porc = float(taxaJuros/100)*depositoInicial
cont = 0
depositoFinal = depositoInicial * 2

while depositoInicial <= depositoFinal:
  cont+=1
  depositoInicial += porc
  # print('{:.2f}'.format(depositoInicial))
  porc = float(taxaJuros/100)*depositoInicial

print(cont)