f = open("1.txt").read().split()

a = []
m = ""

for x in f:
    ok = 1
    for c in x:
        if c not in "0123456789abcdefABCDEF":
            ok = 0

    if ok:
        v = int(x, 16)

        if v <= 4095 and v % 2 == 1 and len(x) > 3:
            a.append(x)

            if m == "" or v < int(m, 16):
                m = x

print(*a)
print(len(a))

for c in m:
    print(c, end="")

