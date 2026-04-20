f = open('1.txt').read().split()
d = {'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
for a in f:
    if a.isdigit() and int(a) % 2==0 and len(a) <= 7:
        print(''.join(d[a[i]] if i % 2 == 0 and int(a[i]) % 2 == 0 else a[i] for i in range(len(a))))
        
    

