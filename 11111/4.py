f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
for a in f:
    if a[0] in ['"', "'", "“", "”"]:
        a = a[1:-1]
        parts = a.split('.')
        print(''.join(d[c] if c.isdigit() else c for c in parts[0]))
