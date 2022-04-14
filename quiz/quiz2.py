def main():
    print('Qual desses não é uma linguagem de programação?\nA - Python\nB - HTML\nC - JavaScript')
    resposta = input().upper()
    score = 0

    if resposta == 'A':
        print(':( Errouuuu')
    elif resposta == 'B':
        print(':) Acertouu')
        score+=1
    elif resposta == 'C':
        print(':( Errouuuu')
    else:
        print('Opção inválida!')

    print('Qual desses não é um banco de dados?\nA - Mongo\nB - Mysql\nC - Oraclu')
    resposta2 = input().upper()

    if resposta2 == 'A':
        print(':( Errouuuu')
    elif resposta2 == 'B':
        print(':( Errouuuu')
    elif resposta2 == 'C':
        print(':) Acertouu')
        score+=1
    else:
        print('Opção inválida!')

    if score == 2:
        print('MUITO BEM!! Obrigada por jogar com a KeyGames')
    else:
        print('TENTE NOVAMENTE!! Obrigada por jogar com a KeyGames')

if __name__ == '__main__':
    main()



