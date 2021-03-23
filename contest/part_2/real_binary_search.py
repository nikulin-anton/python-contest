from math import sqrt


def function(x):
    return x ** 2 + sqrt(x)


def real_binary_search(value):
    max_count = 100
    left = 1.0
    right = 10 ** 10

    for i in range(max_count):
        middle = (right + left) / 2

        if value <= function(middle):
            right = middle
        else:
            left = middle

    return format(right, ".6f")


value = float(input())
result = real_binary_search(value)

print(result)