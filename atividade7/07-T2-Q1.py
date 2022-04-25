def main():
  nome = (input().strip())
  conjuge = ''
  estadoCivil = int(input())
  if estadoCivil == 1:
    conjuge = input()
    tamNome1 = len(nome.replace(" ", ""))
    tamNome2 = len(conjuge.replace(" ", ""))
    print(tamNome1+tamNome2)
  elif estadoCivil == 2:
    tamNome = len(nome.replace(" ", ""))
    print(tamNome)
  else:
    print('inválido')

if __name__ == '__main__':
  main()