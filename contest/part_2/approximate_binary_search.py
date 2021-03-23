def approximate_binary_search(array, value):
    left = 0
    right = len(array)

    while right - left > 1:
        middle = (right + left) // 2

        if value < array[middle]:
            right = middle
        else:
            left = middle

    if left == len(array) - 1 or (value - array[left]) <= (array[left + 1] - value):
        return array[left]

    return array[left + 1]


def get_array_from_input():
    return [int(val) for val in input().split()]


def main():
    [sorted_array_length, numbers_array_length] = get_array_from_input()
    sorted_array = get_array_from_input()
    numbers_array = get_array_from_input()

    for num in numbers_array:
        print(approximate_binary_search(sorted_array, num))


main()

assert approximate_binary_search([1, 3, 5, 7, 9], 2) == 1
assert approximate_binary_search([1, 3, 5, 7, 9], 3) == 3
assert approximate_binary_search([1, 3, 5, 7, 9], 8) == 7
assert approximate_binary_search([1, 3, 5, 7, 9], 1) == 1
assert approximate_binary_search([1, 3, 5, 7, 9], 6) == 5
assert approximate_binary_search([-123, -34, -23, -1, 0, 31, 124, 126], 125) == 124
assert approximate_binary_search([-123, -34, -23, -1, 0, 31, 124, 126], -51) == -34
assert approximate_binary_search([-123, -34, -23, -1, 0, 31, 124, 126], 88) == 124
assert approximate_binary_search([-123, -34, -23, -1, 0, 31, 124, 126], 126) == 126
