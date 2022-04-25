def main():
  peso = float(input())
  altura = float(input())
  imc = peso/(altura*altura)
  print("%.0f" % imc)
  if imc < 18.5:
    print('Abaixo do peso')
  elif imc < 25:
    print('Peso normal')
  elif imc < 30:
    print('Sobrepeso')
  elif imc < 40:
    print('Obeso moderado')
  elif imc >=40:
    print('Obeso mórbido')

if __name__ == '__main__':
  main()






