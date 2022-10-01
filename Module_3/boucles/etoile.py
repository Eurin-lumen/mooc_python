""" trace une étoile à n côtés, si elle peut l'être sans lever la plume"""
import turtle
from math import gcd  # fonction  du module qui calcule le pgcd de deux nombres
LONGUEUR = 300 # Taille de chaque segment
n = int(input("Combien de branches désirez-vous ? : "))
inc = (n - 1) // 2
while gcd(n, inc) > 1:
    inc = inc - 1
if inc == 1:
    print("Impossible de dessiner une étoile à", n, "branches en un tenant")
else:
    angle = 180 - (n - 2 * inc) * 180 / n
    for i in range(n):
        turtle.forward(LONGUEUR)
        turtle.left(angle)
    turtle.done()
