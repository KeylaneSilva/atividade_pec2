dia = int(input().strip())
mes = int(input().strip())
ano = int(input().strip())

dia2 = int(input().strip())
mes2 = int(input().strip())
ano2 = int(input().strip())

result = (f"{dia}/{mes}/{ano}")
result2 = (f"{dia2}/{mes2}/{ano2}")

if (dia > dia2) or (mes > mes2) or (ano > ano2):
    print(result)
else:
    print(result2)