def calcTempo(tempo):
    horas = (tempo/3600)
    resto = tempo%3600
    m = resto/60
    s = resto%60
    print('{:.0f}'.format(horas)+':'+'{:.0f}'.format(m)+':'+ '{:.0f}'.format(s))
seg = int(input())
calcTempo(seg)
