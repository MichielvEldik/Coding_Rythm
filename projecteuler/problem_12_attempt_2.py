"""
1. generate triangles
2. generate prime numbers




"""
import math


def tri_gen():
    """
    Generate triangle numbers
    """
    start = 0
    count = 1
    while True:
        yield int(start + count)
        start = start + count
        count += 1

list = []
for a in tri_gen():
    if a > 99999999:
        break
    list.append(a)

print(list[-1])
