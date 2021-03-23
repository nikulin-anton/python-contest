def binary_search(array, value):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (right + left) // 2

        if value <= array[middle]:
            right = middle
        else:
            left = middle

    if right >= len(array) or value != array[right]:
        return "NO"

    return "YES"


def get_array_from_input():
    return [int(val) for val in input().split()]


def main():
    [sorted_array_length, numbers_array_length] = get_array_from_input()
    sorted_array = get_array_from_input()
    numbers_array = get_array_from_input()

    for num in numbers_array:
        print(binary_search(sorted_array, num))


main()

NO = "NO"
YES = "YES"

assert binary_search([1, 5, 6, 7, 11, 123], 7) == YES
assert binary_search([1, 5, 6, 7, 11, 123], 9) == NO
assert binary_search([1, 5, 6, 7, 11, 123], 4123) == NO
assert binary_search([1, 5, 6, 7, 11, 123], -12) == NO
assert binary_search([1, 5, 6, 6, 6, 11, 123], 6) == YES
assert binary_search([], 2) == NO
assert binary_search([-123, -21, -3, 0, 12, 35, 325, 689], 0) == YES