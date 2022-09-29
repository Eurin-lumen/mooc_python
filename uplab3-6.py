import math
a = float(input())
b = float(input())
if a < 0 or b < 0:
    print("Erreur")
elif a > 0 and b > 0:
    print(math.sqrt(a * b))