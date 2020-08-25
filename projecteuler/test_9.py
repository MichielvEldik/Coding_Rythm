import math


def produce_arb_list():
    prod_list = []
    for i in range(1, 11):
        for e in range(1, 11):
            prod_list.append([i**2, e**2])
    return prod_list

def filter_smaller_b4_bigger(prod_list):
    for a in prod_list:
        if a[0] > a[1]:
            prod_list.remove(a)
    return prod_list

def filter_sum_sqrt(prod_list):
    new_list = []
    for b in prod_list:
        new_list.append([b[0], b[1], sum(b)]) 
    print(new_list)
            
prod_list = produce_arb_list()
print(prod_list)
filter_smaller_b4_bigger(prod_list)
print(prod_list)
print(type(prod_list))
filter_sum_sqrt(prod_list)

