import random

saldo = 10
inzet = []

while saldo > 0 or inzet != []:
    inputtext = input("Op welk nummer wilt u inzetten? 1-36")
    
    try:
        inzet.append(int(inputtext))
        saldo = saldo -1
    except:
        ""

    if inputtext == "STOP" or saldo == 0:
        print("rien ne va plus")
        rand = random.randint(1, 36)
        print("Het nummer was: {}".format(rand))

        for num in inzet:
            if rand == num:
                saldo = saldo + 35
        inzet = []
        print("Uw saldo is nu: {}".format(saldo))

print("GAME OVER")