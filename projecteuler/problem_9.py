import math


def produce_arb_list():
    prod_list = []
    for i in range(1, 1111):
        for e in range(1, 1111):
            prod_list.append([i**2, e**2])
    return prod_list


def if_sum_sqrt(prod_list):
    prod_list = [a for a in prod_list if sum(a) % math.sqrt(sum(a)) == 0]
    prod_list = [a for a in prod_list if a[0] < a[1]]
    for i in prod_list:
        i.append(sum(i))
    return prod_list


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
prod_list = if_sum_sqrt(prod_list)

# take the square root of all numbers in a list and replace the list entirely
another_function(prod_list)

# sum a + b + c and append every sub-list with a value 'd' that represents this sum
sum_function(prod_list)

# find a match for d with 10000
find_1000(prod_list)





