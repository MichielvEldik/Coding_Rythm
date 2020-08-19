"""
sum of the even-valued terms in the Fibonnaci sequence up to 4 million.

"""
#
# Example of a BAD recusrive function.
# This function must make a lot of (unnecessary) recursive calls.
# By caching values we could solve this.
#
# def fibonacci(n):
#     if n ==1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
# for n in range (1, 101):
#     print(n, ":", fibonacci(n))
#
#
#
# example of a good fibonacci sequence algorithm

fibonacci_cache = {}


def fibonacci(n):
    """
    This Fibonacci sequence actually works because it uses value caches.
    This helps us avoid having to run the same sequence twice.
    """
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


sum_list = []
for n in range(1, 34):
    if fibonacci(n) % 2 == 0:
        sum_list.append(fibonacci(n))

    print(n, ":", fibonacci(n))
print(sum(sum_list))  # Answer: 4613732
