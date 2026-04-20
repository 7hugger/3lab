f = open('1.txt').read().split()
d = {'0':'ноль','2':'два','4':'четыре','6':'шесть','8':'восемь'}
for a in f:
    if a.isdigit() and int(a[0]) % 2 == 1 and len(a) <= 5:
        s = ''
        for c in a:
            if c in d:
                s += d[c]
            else:
                s += c
        print(s)
