f = open('1.txt').read().split()
d = {'0':'ноль','1':'один'}
s = []
for a in f:
    b = True
    for c in a:
        if c not in '01':
            b = False
    if b and int(a,2) <= int('1023'):
        s.append(a)
    else:
        if s:
            m = min(s, key=lambda x: int(x,2))
            print(''.join(d[c] for c in m))
            s = []
