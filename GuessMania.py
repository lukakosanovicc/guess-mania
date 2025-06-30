import random

class Grad:
    def __init__(self, ime, drzava, populacija, povrsina):
        self.ime = ime
        self.drzava = drzava
        self.populacija = int(populacija)
        self.povrsina = int(povrsina) # int cisto radi lakseg pogadjanja

def Ucitaj(ime_fajla: str) -> List[Grad]:
    gradovi = []
    try:
        with open(ime_fajla, "r") as fajl:
            for linija in fajl:
                linija = linija.strip()
                if linija:
                    delovi = linija.split("|")
                    if len(delovi) >= 4:
                        grad = Grad(delovi[0], delovi[1], delovi[2], delovi[3])
                        gradovi.append(grad)
    except FileNotFoundError:
        print(f"Greska: fajl '{ime_fajla}' nije pronadjen.")
    return gradovi

def Proveri(tacna_vrednost, pokusaj, tolerancija=0.15) -> bool: # tolerancija se moze menjati
    donja_granica = tacna_vrednost * (1 - tolerancija)
    gornja_granica = tacna_vrednost * (1 + tolerancija)
    return donja_granica <= pokusaj <= gornja_granica

def Igraj() -> None:
    if not gradovi:
        print("--> Nema dostupnih podataka za igru.")
        return

    print("============= Dobrodosli u GuessMania! =============")

    random.shuffle(gradovi)

    for grad in gradovi:
        print(f"\n>> Grad: {grad.ime} ({grad.drzava})")
        print("Šta zelite da pogadjate?")
        print("\n1. Populaciju")
        print("2. Povrsinu")
        izbor = input("\nUnesite 1 ili 2: ").strip()

        if izbor not in ["1", "2"]:
            print("--> Nevazeci izbor. Kraj igre.")
            break

        try:
            unos = int(input("Unesite Vasu procenu: "))
        except ValueError:
            print("--> Nevazeci unos. Molimo unesite broj. Kraj igre.")
            break

        if izbor == "1":
            odgovor = grad.populacija
        else:
            odgovor = grad.povrsina

        if Proveri(odgovor, unos):
            print(f"Tacno! Prava vrednost je {odgovor}")
        else:
            print(f"Netacno. Prava vrednost je {odgovor}")
            print("Kraj igre.")
            break
    else:
        print("\nBravo! Pogodili ste sve gradove!")

if __name__ == "__main__":
    gradovi = Ucitaj("data.txt")
    Igraj()
