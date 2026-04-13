import re

f = open("1.txt").read()

a = []
m = ""

nums = re.findall(r"[0-9A-Fa-f]+", f)

for x in nums:
    v = int(x, 16)

    if v <= 4095 and v % 2 == 1 and len(x) > 3:
        a.append(x)

        if m == "" or v < int(m, 16):
            m = x

print(*a)
print(len(a))

for c in m:
    print(c, end="")

