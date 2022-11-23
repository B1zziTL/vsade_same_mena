#zadeklarovanie premennej a zoznamov
pocitadlo = 0
krstne_mena = []
priezviska = []

#jednorazove otvorenie suboru na spocitanie riadkov
with open("mena_zamestnancov.txt","r") as subor:
    riadky = len(subor.readlines())

#otvorenie suboru na citanie
subor = open("mena_zamestnancov.txt","r")

for riadok in subor: #cyklus na zaradenie mien do zoznamov
    #zmena pomocnej premennej
    pocitadlo += 1

    #vymazanie nepodstatnych znakov z riadku
    riadocek = riadok.strip()

    #prva polovica suboru sa ulozi do krstnych mien, druha polovica do priezvisk
    if pocitadlo <= (riadky/2):
        krstne_mena.append(riadocek)
    else:
        priezviska.append(riadocek)

#zistenie najdlhsieho krstneho mena a priezviska
krstne_meno = max(krstne_mena, key=len)
priezvisko = max(priezviska, key=len)

#zatvorenie suboru
subor.close()

#otvorenie suboru na pisanie
subor1 = open("vystup.txt","w")

for i in range(int(riadky/2)): #cyklus na vypisanie do vystupneho suboru
    #vypocet potrebnej medzery
    medzery = len(krstne_meno) - len(krstne_mena[i])
    medzera = " " * (medzery+1)

    #vypisanie hodnot do riadku
    subor1.write(krstne_mena[i]+medzera+priezviska[i]+"\n")

#zatvorenie suboru
subor1.close()

#vypisanie pozadovanych informacii
print("Počet mien:",int(riadky/2))
print("Najdlhšie krstné meno:",krstne_meno)
print("Najdlhšie priezvisko:",priezvisko)
