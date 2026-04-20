f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь'}
for a in f:
    b = True
    for c in a:
        if c not in '01234567':
            b = False
    if b and int(a) % 2 == 0 and int(a[0]) % 2 == 1 and len(a) > 3:
        used = []
        for c in a:
            if a.count(c) > 1 and c not in used:
                print(d[c], end=' ')
                used.append(c)
        print()
