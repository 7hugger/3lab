f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
for a in f:
    if a.isdigit():
        b = True
        for i in range(len(a)-1):
            if int(a[i]) % 2 == int(a[i+1]) % 2:
                b = False
        if b:
            print(d[min(a)], d[max(a)])
