import random

say=0
asal=[]
temp1=[]
temp2=[]
temp3=[]
control=0

sayi = list(range(101))
random.shuffle(sayi)

for i in sayi:
    if i<2:
        continue                   #1 in asal olmadığı kabul edilir.
    else:
        if(i==2):
             control=0             #2'nin asal olduğu kabul edilir.
                                   #ayrıca range(2,2) den kaçınmak istedim
        else:
            for j in range(2,i):
                if(i%j==0):
                    control=1      # asal olmadığı anlaşılır.

        if(control!=1):
            if(say<3):
                temp1.append(i)
            elif(say<6):
                temp2.append(i)
            else:
                temp3.append(i)

            say+=1
        else:
            control=0

    if(say==9):
        asal=zip(temp1,temp2,temp3)
        break
    else:
        continue

for i in asal:
    print(i)
