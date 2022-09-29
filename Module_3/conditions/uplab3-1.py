a = int(input())
b = int(input())
c = int(input())
controle = a == b or a == c or b == c
if controle:
    print(a or b or c)
else:
    print()