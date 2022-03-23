class Shaxs:
    def __init__(self, ism, familya, pasport, tyil):
        """ Shaxsning xususiyatlari """
        self.ism = ism
        self.familya = familya
        self.pasport = pasport
        self.tyil = tyil

    def get_info(self):
        info = f"{self.ism} {self.familya}. "
        info += f"Pasport {self.pasport} {self.tyil}-yilda tug'ilgan"
        return info
    def get_age(self, yil):
        age = yil - self.tyil
        return age

class Talaba(Shaxs):
    def __init__(self, ism, familya, pasport, tyil, idraqam, manzil):
        super().__init__(ism, familya, pasport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
class Manzil:
    def __init__(self, uy, kocha, shaxar, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.shaxar = shaxar
        self.viloyat = viloyat

    def get_manzil(self):
        manzil = f"{self.viloyat} viloyat {self.shaxar} shaxar {self.kocha} kocha {self.uy} - uy"
        return manzil
talaba_manzil = Manzil(14, "lola", "marg'ilon", "fargona")
# talaba_manzil = Manzil(14, "Lola", "Marg'ilon", "Farg'ona")
student = Talaba("Absu", "ksd", "skdj", 2000, "sdkksjd200", talaba_manzil)

print(student.manzil.get_manzil())