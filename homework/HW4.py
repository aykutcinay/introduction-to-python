import random

class words():

    def __init__(self):

        k1="hastane"
        k2="otomobil"
        k3="rasathane"
        k4="mercimek"
        k5="telefon"

        liste=[k1,k2,k3,k4,k5]

        can=5

        print("WELCOME TO HANGBANG")
        print("HARF TAHMİNİNE BAŞLA")
        print("UNUTMA SADECE 5 CANIN VAR")
        num=random.randint(0,4)

        print("_ "*len(liste[num]),  "    CAN {}".format(can))
        a=["_" for i in range(len(liste[num]))]

        print(a)

        while True:
            harf=input("HARF ALİM :)     ")

            if harf in liste[num]:
                for i in liste[num]:
                    if(i==harf):

                        b=[t for t,i in enumerate(liste[num]) if i==harf]
                        for s in range(len(b)):
                              a[b[s]]=harf
            else:
                can-=1
                if(can==0):
                    print("CANINIZ KALMADI...")
                    break
            print(a)

            if(not "_" in a):
                print("TEBRİKLER KELİMEYİ BULDUNUZ")
                break
            else:
                continue

kelime=words()
