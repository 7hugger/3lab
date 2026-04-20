f = open('1.txt').read().split()
for a in f:
    if a.isdigit():
        if len(set(a)) == 1:
            print(a, 'единиц')
        else:
            print(a[::-1])
