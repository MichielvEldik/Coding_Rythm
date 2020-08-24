"""
Pythagoras triplets
"""

import math
import numpy

prod_list = []

for i in range(1, 1111):
    for e in range(1, 1111):
        prod_list.append([i**2, e**2])

new_list = []
for a in prod_list:
    if a[0] < a[1]:
        new_list.append(a)

a_list = []
for b in new_list:
    if sum(b) % math.sqrt(sum(b)) == 0:
        a_list.append(b)

for x in a_list:
    x.append(sum(x))

last_list = []
for a in a_list:
    temp_list = []
    for e in a:
        temp_list.append(math.sqrt(e))
    last_list.append(temp_list)

for g in last_list:
    g.append(sum(g))

for m in last_list:
    if m[3] == 1000.0:
        print(math.prod(m))
