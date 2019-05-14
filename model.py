
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+', 
PONOVLJENA_CRKA = 'o' 
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo
        self.crke = []
    
    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]


igra = Igra("nekaj")
igra.crke = ['a', 'l', 'v', 'n', 'x']
print(igra.napacne_crke())
print(igra.pravilne_crke())