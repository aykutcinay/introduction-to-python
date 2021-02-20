def prime_first(i):

    control=0
    if i>=2:
        if(i==2):
             print(i)
        else:
            for j in range(2,i):
                if(i%j==0):
                    control=1

        if(control!=1):
            print(i)
            control=0

def prime_second(i):
    control=0
    for j in range(2,i):
        if(i%j==0):
                    control=1
    if(control!=1):
        print(i)
        control=0

for i in range(0,1001):
        if i<=500:
            prime_first(i)
        else:
            prime_second(i)


