number = 60000000

tri_number = number * (number + 1) / 2
print(tri_number)
lijstje = []
for i in range(1, number):
    if number % i == 0:
        lijstje.append(i)
print(len(lijstje))
