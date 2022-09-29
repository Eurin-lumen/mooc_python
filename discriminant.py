a = float(input('a : '))
b = float(input('b : '))
c = float(input('c : '))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print(" pas de racines réelles")
elif delta == 0:
    print("une racine : ")
    print("x = ", -b / (2 * a))
else:
    racine = delta ** 0.5
    print("deux racines : ")
    print("x1 = ", (-b + racine) / (2 * a))
    print("x2 = ", (-b - racine) / (2 * a))
