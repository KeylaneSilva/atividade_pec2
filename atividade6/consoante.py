def main():
    caractere = input().lower()
    if caractere in ['a','e','i','o','u', '/', '0']:
        print('False')
    else:
        print('True')

if __name__ == '__main__':
    main()