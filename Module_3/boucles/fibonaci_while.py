n = int(input('borne supérieur à ne pas dépasser pour calculer la suite de Fibonacci : '))
prec = 0
succ = 1
print(prec, end = ' ')
while succ < n :
    print(succ, end = ' ')
    prec, succ = succ, prec + succ
print()