"""
Task: Loops

https://www.hackerrank.com/challenges/python-loops/problem

the code reads an integer. for all non-negative integers i < n, print i**2.
e.g. n = 3 is [0, 1, 2]


"""

N = 5

for i in range(N):
    if i < N:
        print(i**2)
