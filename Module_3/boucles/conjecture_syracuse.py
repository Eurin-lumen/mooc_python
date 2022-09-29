n = int(input('entier strictement positif : '))
while n != 1 and n > 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
print(n)  # imprime