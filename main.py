'''
4. Feladat
Írj egy programot while ciklussal, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
'''
beker = int(input('hanyszor? :'))
bekersz = input('szoveg:  ')
x = 0
while x < beker:
    print(bekersz)
    x+=1