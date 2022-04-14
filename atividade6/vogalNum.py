def main():
    caractere = input().upper()
    if 'A' <= caractere <= 'Z' or '0':
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()