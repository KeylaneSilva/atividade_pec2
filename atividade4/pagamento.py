def avista(valor):
    return valor * 0.91

def parcelado1(valor):
    return valor/5

def parcelado2(valor):
    return (valor/10)*1.17

valor = float(input())
print("%.2f" % avista(valor))
print("%.2f" % parcelado1(valor))
print("%.2f" % parcelado2(valor))
