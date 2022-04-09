def maximo(x1,x2,x3,x4,x5):
    return max(x1,x2,x3,x4,x5)

def minimo(x1,x2,x3,x4,x5):
    return min(x1,x2,x3,x4,x5)

def media(x1,x2,x3,x4,x5):
    return (x1+x2+x3+x4+x5)/5

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

print(f'{maximo(n1,n2,n3,n4,n5)}\n{minimo(n1,n2,n3,n4,n5)}\n{media(n1,n2,n3,n4,n5)}')
