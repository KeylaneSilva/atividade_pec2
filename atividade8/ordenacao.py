from os import remove
from numpy import sign

# função para separar as datas em dia, mes e ano
def separar_data(dma):
  #exemplo 07121999
  # a = 1999
  # dma = dma/10000 = 712.1999
  a = dma % 10000
  dma //=10000

  # 12
  # dma = 7.121999
  m = dma % 100
  dma //=100

  # d = 7
  d = dma
  return d,m,a

# retorna o signo de acordo com a data de nascimento
def signo(dia,mes):
  if mes == 3:
    return 'Peixes' if dia < 21 else 'Aries'
  if mes == 4:
    return 'Aries' if dia < 20 else 'Touro'
  if mes == 5:
    return 'Touro' if dia < 21 else 'Gemeos'
  if mes == 6:
    return 'Gemeos' if dia < 21 else 'Cancer'
  if mes == 7:
    return 'Cancer' if dia < 21 else 'Leao'
  if mes == 8:
    return 'Leao' if dia < 21 else 'Virgem'
  if mes == 9:
    return 'Virgem' if dia < 21 else 'Libra'
  if mes == 10:
    return 'Libra' if dia < 21 else 'Escorpiao'
  if mes == 11:
    return 'Escorpiao' if dia < 21 else 'Sargitario'
  if mes == 12:
    return 'Sargitario' if dia < 21 else 'Capricornio'
  if mes == 1:
    return 'Capricornio' if dia < 21 else 'Aquario'
  if mes == 2:
    return 'Aquario' if dia < 21 else 'Peixes'

# remove os acentos do signo recebido
def remover_acentos(texto):
  from unicodedata import normalize
  return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

# retorna a consulta do horoscopo do dia de acordo com o site do horospocovirtual
def horoscopo(signo_desejado):
  import urllib.request
  signo_formatado = remover_acentos(signo_desejado).lower()
  minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/' + signo_formatado

  requisicao = urllib.request.Request(
    url=minha_url,
    headers={'User-Agent': 'Mozila/5.0'}
  )

  resposta = urllib.request.urlopen(requisicao)
  pagina = resposta.read().decode('utf-8')

  marcador_inicio = '<p class="text-pred">'
  marcador_final = '</p>'

  inicio = pagina.find(marcador_inicio) + len(marcador_inicio)
  final = pagina.find(marcador_final, inicio)

  return signo_desejado + ': ' + pagina[inicio:final]

def main():
  #entrada de dados
  nascimento = int(input("Digite sua data de nascimento no formato DDMMAAAA: "))

  #processamento
  dia, mes, ano = separar_data(nascimento)
  meu_signo = signo(dia,mes)
  horoscopo_de_hoje = horoscopo(meu_signo)

  #saída de dados
  print(horoscopo_de_hoje)


if __name__ == '__main__':
  main()