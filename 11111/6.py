f = open('1.txt').read().split()
d = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
for i in range(len(f)):
    a = f[i]
    if a.isdigit() and int(a) % 2 == 1 and len(a) <= 8 and i % 2 == 0 and int(a[0]) % 2 == 0:
        a = d[a[0]] + a[1:]
        print(a)
    else:
        print(a)
