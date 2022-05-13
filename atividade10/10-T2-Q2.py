# idade = int(input().strip())
# pessoas = 0
# media = 0
# menorIdade = idade
# maiorIdade = 0
# totIdade = 0

# if idade == 0:
#   exit()

# while idade != 0:
#   pessoas+=1
#   idade = int(input().strip())
#   totIdade+=idade

#   if idade == 0:
#     break

#   if idade > maiorIdade:
#     maiorIdade = idade

#   if idade < menorIdade:
#     menorIdade = idade

# print(pessoas)
# media = totIdade/(pessoas-1)
# print('{:.2f}'.format(media))
# print(menorIdade)
# print(maiorIdade)

def menor(idade1, idade2):
    return idade1 if idade1 < idade2 else idade2

def maior(idade1, idade2):
    return idade1 if idade1 > idade2 else idade2

qtd_pessoas = 0

soma = 0

idade = int(input())

maior_idade = -999999999

menor_idade = 999999999

while idade != 0:
    qtd_pessoas += 1

    maior_idade = maior(idade, maior_idade)

    menor_idade = menor(idade, menor_idade)

    soma += idade

    idade = int(input())

if soma != 0:
    media_idade = soma / qtd_pessoas
    print(f'{qtd_pessoas}')
    print(f'{media_idade:.2f}')
    print(f'{menor_idade}')
    print(f'{maior_idade}')

