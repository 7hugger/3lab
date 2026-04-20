f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь'}
for a in f:
    if a in '1234567' and int(a[-1]) % 2 == 0 and int(a[0]) % 2 == 0 and len(a) <= 3:
        print(d[min(a)], d[max(a)])
