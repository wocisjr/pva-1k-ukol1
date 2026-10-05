import random

pokusy = 1
number = random.randint(1, 100)
tvujdifficulty = int(input("Vyber si obtížnost: "))

if tvujdifficulty > 3:
    print("Neplatná obtížnost, zvol si číslo 1, 2 nebo 3.")
    exit()

if tvujdifficulty == 1:
    number = random.randint(1, 100)
if tvujdifficulty == 2:
    number = random.randint(1, 1000)
if tvujdifficulty == 3:
    number = random.randint(1, 5000)

while True:
    tvujguess = int(input("Hádej číslo: "))
    pokusy += 1

    if tvujguess < number:
        print("Hádej výš \nPočet pokusů:", pokusy,"\n")

    elif tvujguess > number:
        print("Hádej níž \nPočet pokusů:", pokusy,"\n")

    else:
        print("Uhodl jsi správně, je to číslo", number)
        break
