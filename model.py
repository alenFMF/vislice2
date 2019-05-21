
import random
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+' 
PONOVLJENA_CRKA = 'o' 
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

with open('vaja11/vislice2/besede.txt') as f:
    bazen_besed = [beseda.strip() for beseda in f.readlines()]

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo.upper()
        self.crke = []
    
    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(c in self.crke for c in self.geslo)

    def poraz(self):
        return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        # return "".join(c if c in self.crke else '_' for c in self.geslo)
        novi = ''
        for c in self.geslo:
            if c in self.crke:
                novi += c
            else:
                novi += '_'
        return novi

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        if crka in self.geslo.upper():
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            return PRAVILNA_CRKA
        # potem je napačna neponovljena
        self.crke.append(crka)
        if self.poraz():
            return PORAZ
        return NAPACNA_CRKA
        

def nova_igra():   
    geslo = random.choice(bazen_besed)
    return Igra(geslo) 

nova_igra()        
# print(bazen_besed[0])
# print(bazen_besed[-1])

# igra = Igra("nekaj")
# igra.crke = ['A', 'L', 'V', 'N', 'X', 'E']
# print(igra.napacne_crke())
# print(igra.pravilne_crke())
# print(igra.stevilo_napak())
# print(igra.zmaga())
# print(igra.poraz())
# print(igra.pravilni_del_gesla())
# print(igra.nepravilni_ugibi())
# print("Ugibam k")
# print(igra.ugibaj('k'))
# print(igra.pravilni_del_gesla())
# print(igra.nepravilni_ugibi())
# print("Ugibam v")
# print(igra.ugibaj('v'))
# print(igra.pravilni_del_gesla())
# print(igra.nepravilni_ugibi())
# print("Ugibam f")
# print(igra.ugibaj('f'))
# print(igra.pravilni_del_gesla())
# print(igra.nepravilni_ugibi())
