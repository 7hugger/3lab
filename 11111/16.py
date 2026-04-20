f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять'}
for a in f:
    if a in '012345' and int(a) % 2 == 1 and int(a[0]) % 2 == 1 and len(a) > 3:
        print(d[min(a)], d[max(a)])
