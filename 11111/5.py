f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
for i in range(len(f)):
    a = f[i]
    if a.isdigit() and int(a) % 2 == 0 and len(a) <= 5 and i % 2 == 0:
        print(''.join(d[c] for c in a))
    else:
        print(a)
