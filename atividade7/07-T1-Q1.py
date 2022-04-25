def main():
  diaA = int(input().strip())
  mesA = int(input().strip())
  anoA = int(input().strip())

  diaN = int(input().strip())
  mesN = int(input().strip())
  anoN = int(input().strip())

  if mesA < mesN:
    print((anoA - anoN) - 1)
  elif mesA == mesN:
    if(diaN >= diaA):
      print(anoA - anoN)
  else:
    print(anoA - anoN)


if __name__ == '__main__':
  main()



