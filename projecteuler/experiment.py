import math


def produce_arb_list():
    prod_list = []
    for i in range(1, 11):
        for e in range(1, 11):
            prod_list.append([i**2, e**2])
    return prod_list


def if_sum_sqrt(prod_list):

    for a in prod_list:
        if a[0] > a[1]:
            prod_list.remove(a)
    print(prod_list)
    for b in prod_list:
        if sum(b) % math.sqrt(sum(b)) != 0:
            prod_list.remove(b)
            prod_list.append(sum(b))
    print(prod_list)


def another_function(prod_list):
    for lists in prod_list:
        for p, i in enumerate(lists):
            lists[p] = math.sqrt(i)


def sum_function(prod_list):
    for b in prod_list:
        b.append(sum(b))


def find_1000(prod_list):
    for m in prod_list:
        if m[3] == 1000:
            print(math.prod(m))


# generate an arbitrary list with squared numbers
prod_list = produce_arb_list()

# filter out any sets for which their sum is not a perfect square
# filter out any sets for which the first number (a^2) is larger than the second (b^2)
# after all, we want to adhere to a < b < c
# Lastly, append sum of the filtered sets and add this sum as
if_sum_sqrt(prod_list)

# take the square root of all numbers in
another_function(prod_list)

sum_function(prod_list)

find_1000(prod_list)





