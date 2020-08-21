"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
number = 20


def divide_checker(i, s):
    if s % i == 0:
        return True

holding_answer = []
for y in range(1, 3000):
    for b in range(1, 21):
        if divide_checker(b, y) is True:
            if divide_checker(b +1, y) is True:
                if divide_checker(b+2, y) is True:
                    print(b, b+1, b+2, y)



