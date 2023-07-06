# Napraviti program koji baca 3 kockice i računa koliko put moramo baciti kockice da bi dobili iste brojeve
# Vratiti broj koraka od prve iteracije do druge
from random import randrange

koraci = 0
koraciDoDrugeIteracije = 0
vracenoPuta = 0
kraj = False
prvaIteracija = [0,0,0]
drugaIteracija = [0,0,0]

def BaciKockice():
    broj1 = randrange(10)
    broj2 = randrange(10)
    broj3 = randrange(10)
    if broj1 == broj2 == broj3:
        # Dodavanje kombinacija za svaku iteraciju
            if vracenoPuta == 1:
                drugaIteracija[0] = broj1
                drugaIteracija[1] = broj2
                drugaIteracija[2] = broj3
                if prvaIteracija[0] == drugaIteracija[0] and prvaIteracija[1] == drugaIteracija[1] and prvaIteracija[2] == drugaIteracija[2]:
                    print(f"* Kombinacija ovaj put je bila {broj1} {broj2} {broj3} i to su isti brojevi sto znaci da je iteracija zavrsena.")
                    return True
            elif vracenoPuta == 0:
                prvaIteracija[0] = broj1
                prvaIteracija[1] = broj2
                prvaIteracija[2] = broj3
                print(f"* Kombinacija ovaj put je bila {broj1} {broj2} {broj3} i to su isti brojevi sto znaci da je iteracija zavrsena.")
                return True
    else:
        # print(f"* Kombinacija ovaj put je bila {broj1} {broj2} {broj3}")
        return False

kombinacija = BaciKockice()

while kraj == False:
    if kombinacija == True:
        if vracenoPuta == 1 and koraciDoDrugeIteracije != 0:
            if prvaIteracija[0] == drugaIteracija[0] and prvaIteracija[1] == drugaIteracija[1] and prvaIteracija[2] == drugaIteracija[2]:
                vracenoPuta += 1
                kraj = True
                print(f"-> Koraka potrebnih do iste kombinacije u drugoj iteraciji bilo je: {koraciDoDrugeIteracije}")
            else:
                kombinacija = False
                print(f"-> Koraka potrebnih do iste kombinacije bilo je: {koraci}")
        elif vracenoPuta == 0:
            vracenoPuta += 1
            kombinacija = False
            print(f"-> Koraka potrebnih do iste kombinacije bilo je: {koraci}")
    else:
        kombinacija = BaciKockice()
        if vracenoPuta == 1:
            koraciDoDrugeIteracije += 1
        else:
            koraci += 1
else:
    if vracenoPuta == 1 and koraciDoDrugeIteracije != 0:
            if prvaIteracija[0] == drugaIteracija[0] and prvaIteracija[1] == drugaIteracija[1] and prvaIteracija[2] == drugaIteracija[2]:
                vracenoPuta += 1
                kraj = True
                print(f"-> Koraka potrebnih do iste kombinacije u drugoj iteraciji bilo je: {koraciDoDrugeIteracije}")
            else:
                kombinacija = False
                print(f"-> Koraka potrebnih do iste kombinacije bilo je: {koraci}")
    elif vracenoPuta == 0:
        vracenoPuta += 1
        kombinacija = False
        print(f"-> Koraka potrebnih do iste kombinacije bilo je: {koraci}")