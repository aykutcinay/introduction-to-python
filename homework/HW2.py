temp_list_ad=[]
temp_list_note=[]
midterm=0
final=0
homework=0
ad=""
soyad=""
notes =[ ]
names =[ ]
info={}
not_ort=[]

for i in range(5):
    for j in range(1):

        print("{}. Öğrenci Bilgileri" .format(i+1))

        ad=input("Adı       :   ")
        soyad=input("Soyadı    :   ")

        midterm = int(input("midterm   :   "))
        final= int(input("final     :   "))
        homework=int(input("homework  :   "))

        print("-------------------------------")
        temp_list_ad=[ad,soyad]
        temp_list_note=[midterm,final,homework]

    names.append(temp_list_ad)
    notes.append(temp_list_note)

for i in range(5):
    info[(names[i][0]+" "+names[i][1])]=("midterm= "+ str(notes[i][0])+" final= "+ str(notes[i][1])+" homework= "+ str(notes[i][2]))

for key,value in info.items():
    print(key ," ", value,  )

print("   ")

for i in range(5):
    not_ort.append((notes[i][0]+notes[i][1]+notes[i][2])/3)

print("Not Ortalamaları",not_ort)

maxnote_index=not_ort.index(max(not_ort))

print("   ")
print("Tebrikler {} {} ".format(names[maxnote_index][0],names[maxnote_index][1]))
print("En yüksek ortalamaya sahipsiniz !!!")
