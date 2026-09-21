import random

pokusy = 1
number = random.randint(1, 100)
tvujguess = int(input("Hádej číslo: "))

while True:
    tvujguess = int(input("Hádej číslo: "))

    if tvujguess < number:
        print("Hádej výš")

    elif tvujguess > number:
        print("Hádej níž")

    else:
        print("Uhodl jsi správně, je to číslo", number)
        break
