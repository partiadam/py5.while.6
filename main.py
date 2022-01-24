'''
6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
'''

from random import randint


x = 0
while x <20:
    szam = randint(1,12)
    if szam %3 == 0:
        print(szam)
    x += 1
    