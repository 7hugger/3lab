f = open('1.txt').read().split()
d = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','A':'ten','B':'eleven','C':'twelve','D':'thirteen','E':'fourteen','F':'fifteen'}
max_num = '0'
for a in f:
    ok = True
    for c in a:
        if c not in '0123456789ABCDEF':
            ok = False
    if ok and len(a) <= 5:
        if int(a,16) > int(max_num,16):
            max_num = a
print(' '.join(d[c] for c in max_num))
