"""
Auteur : Eurin d'ALMEIDA
Un jeu de devinette pour l'utilisateur
"""
import random
secret = random.randint(0, 5)
valeur = int(input("Entrer un nombre : "))
if valeur == secret : # il faut avoir une sacré chance pour gagne - 1/6
    print("Vous avez Gagnez")
else :
    print("Vous avez perdu, la valeur etait", secret)