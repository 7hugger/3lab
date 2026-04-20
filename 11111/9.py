f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
count = 0
for a in f:
    if a.isdigit() and '0' in a:
        count += a.count('0')
print(' '.join(d[c] for c in str(count)))
