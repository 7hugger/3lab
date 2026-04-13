import re

d={'0':'ноль','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
t=open("1.txt").read()

for n in re.findall(r'\b[0-9]{1,7}\b', t):
    if int(n)%2==0: print(" ".join(d[c] if int(c)%2==0 and (i+1)%2==1 else c for i,c in enumerate(n)))
