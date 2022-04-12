def sinal_transito():
    cor = input().upper()
    if cor == 'V':
        return 'Siga'
    elif cor == 'A':
        return 'Atenção'
    else:
        return 'Pare'

print(sinal_transito())
