#overlap
#lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]

a1=[]
b1=[]
for d1 in a:
    if d1 not in a1:
        a1.append(d1)
for d2 in b:
    if d2 not in b1:
        b1.append(d2)

for x in a1:
    if x in b1:
        print(x)