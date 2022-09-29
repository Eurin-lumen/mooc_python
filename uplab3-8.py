import math

lettre = input()
a = float(input())
if lettre == "T":
    print((math.sqrt(2) / 12) * a ** 3)
elif lettre == "C":
    print(a ** 3)
elif lettre == "O":
    print((math.sqrt(2) / 3) * a ** 3)
elif lettre == "D":
    print((15 + 7 * math.sqrt(5) / 12) * a ** 3)
elif lettre == "I":
    print((5 * (3 + math.sqrt(5)) / 12) * a ** 3)
else:
    print("Polyèdre non connu")
