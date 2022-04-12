def media_alunos():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    media = (n1+n2+n3)/3

    if n3 > 8:
        new_media = media+1
        if new_media > 10:
            new_media = 10
            return new_media
        else:
            return new_media
    else:
        return media

print("%.2f" % media_alunos())
