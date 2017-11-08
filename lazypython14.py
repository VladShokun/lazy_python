d = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
d[5] = 6
print(d)
dd = {6: 7, 7: 8}
d.update(dd)
print(d)

ddd = {a: a +1 for a in range(8, 15)}
d.update(ddd)
print(d)