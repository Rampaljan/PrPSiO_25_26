import random

def sprawdz_wynik(wybor_gracza, wybor_komputera):
    if wybor_gracza == wybor_komputera:
        return 0
    if (wybor_gracza == "nożyce" and wybor_komputera == "kamień") or (wybor_gracza == "kamień" and wybor_komputera == "papier") or (wybor_gracza == "papier" and wybor_komputera == "nożyce"):
        return -1
    if (wybor_gracza == "kamień" and wybor_komputera == "nożyce") or (wybor_gracza == "papier" and wybor_komputera == "kamień") or (wybor_gracza == "nożyce" and wybor_komputera == "papier"):
        return 1

def uruchom_gre():
    while True:
        wybory = ['papier', 'kamień', 'nożyce']
        punkty_gracz = 0
        punkty_komputer = 0

        wybor_gracza = input("Wpisz swój wybór (papier/kamień/nożyce), lub (koniec) aby zakończyć grę: ")

        if wybor_gracza == "koniec":
            print("Zakończono Grę")
            print(f"Bilans punktów - Gracz: {punkty_gracz}, Komputer: {punkty_komputer}")
            break

        if wybor_gracza in wybory:

            wybor_komputera = random.choice(wybory)
            
            if sprawdz_wynik(wybor_gracza, wybor_komputera) == 0:
                punkty_gracz += 1
                punkty_komputer += 1
                print("Remis")

            if sprawdz_wynik(wybor_gracza, wybor_komputera) == 1:
                punkty_gracz += 1
                print("Wygrałeś")

            if sprawdz_wynik(wybor_gracza, wybor_komputera) == -1:
                punkty_komputer += 1
                print("Przegrałeś")

            print(f"Aktualny bilans punktów - Gracz: {punkty_gracz}, Komputer: {punkty_komputer}")

        else:
            print("Źle wpisałeś swój wybór")