"""
Task: Loops

https://www.hackerrank.com/challenges/python-loops/problem

the code reads an integer. for all non-negative integers i < n, print i**2.
e.g. n = 3 is [0, 1, 2]


"""

n = 5

for i in range (n):
    if i < n:
        print(i**2)

