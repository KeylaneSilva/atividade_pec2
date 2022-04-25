def main():
  nota1 = float(input())
  nota2 = float(input())
  nota3 = float(input())
  nota4 = float(input())
  nota5 = float(input())

  media = float((nota1+nota2+nota3+nota4+nota5)/5)
  print("%.2f" % media)

  if(nota1 > media):
    print("%.2f" % nota1)
  if(nota2 > media):
    print("%.2f" % nota2)
  if(nota3 > media):
    print("%.2f" % nota3)
  if(nota4 > media):
    print("%.2f" % nota4)
  if(nota5 > media):
    print("%.2f" % nota5)

if __name__ == '__main__':
  main()
