f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
count = 0
max_num = 0
for a in f:
    if a.isdigit() and int(a) % 2 == 0 and int(a[0]) % 2 == 1 and len(a) > 3:
        count += 1
        if int(a) > max_num:
            max_num = int(a)
print(count)
print(''.join(d[c] for c in str(max_num)))
