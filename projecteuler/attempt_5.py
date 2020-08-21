
def divide_checker(number):
        listy = []
        list_factors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        factor = 1
        for i in listy:
            if number % i  == 0:
                listy.append(number)
            else:
                break
        if len(listy) == 19:
            return True
        else:
            return False
# print(divide_checker(232792560))

for i in range(1000, 999999999):
    if divide_checker(i) == True:
        print(i)
