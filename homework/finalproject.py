class ön_hazırlık():
     def __init__(self):
        print("1. Malzemeler yıkandı...")
        print("2. Pişirmek için hazırlandı...")

class pişir(ön_hazırlık):
     def __init__(self,dk,derece,yöntem):
        self.dk=dk
        self.derece=derece
        self.yöntem=yöntem
        super().__init__()
        self.pişirildi()

     def pişirildi(self):
         print("3. {} dakika {} derecede {} pişirildi".format(self.dk,self.derece,self.yöntem))

class tavuk_kızartma(pişir):
     def __init__(self,dk,derece):
        yöntem="kızartma"
        super().__init__(dk,derece,yöntem)
        print("4. Kızartılmış tavuk hazır --- Afiyet Olsun !!!")
        print("-----------------------------------")

class tavuk_haşlama(pişir):
     def __init__(self,dk,derece):
        yöntem="haşlama"
        super().__init__(dk,derece,yöntem)
        print("4. Haşlanmış tavuk hazır --- Afiyet Olsun !!!")
        print("-----------------------------------")

class fırında_tavuk(pişir):
    def __init__(self,dk,derece):
        yöntem="fırında"
        super().__init__(dk,derece,yöntem)
        print("4. Fırında tavuk hazır --- Afiyet Olsun !!!")
        print("-----------------------------------")

yemek=fırında_tavuk(30,150)
yemek1=tavuk_haşlama(20,50)
yemek2=tavuk_kızartma(15,60)
