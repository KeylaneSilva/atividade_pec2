def numero():
    caractere = input()
    if '0' < caractere < '9':
        return True
    else:
        return False

print(numero())