import random
pari_joueur = random.randint(0, 16)
data = int(input())
pari_joueur = random.randint(0, 16)
print(pari_joueur)
if (data == 0 or data <=12) and (pari_joueur == data):
    print(data * 12)
elif data == 13 and data % 2 == 0:
    print(data * 2)
elif data == 14 and data % 2 != 0:
    print(data * 2)
elif data == 15 and data % 2 != 0:
    print(data * 2)
elif data == 16 and data % 2 == 0:
    print(data * 2)









