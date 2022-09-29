annee = int(input())
if annee % 400 == 0:
    print('bissextile')
elif annee % 100 == 0:
    print('non bissextile')
elif annee % 4 == 0:
    print('bissextile')
else:
    print('non bissextile')