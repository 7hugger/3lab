f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
count = 0
min_num = None
for a in f:
    if a.isdigit() and int(a) % 2 == 1 and a[0] == '7' and len(a) == 5:
        count += 1
        if min_num is None or int(a) < min_num:
            min_num = int(a)
print(count)
print(''.join(d[c] for c in str(min_num)))
