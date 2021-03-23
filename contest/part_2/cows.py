def can_be_placed(stall_coords, cows_count, distance):
    coord_index = 0

    for cow in range(cows_count - 1):
        target_coord = stall_coords[coord_index] + distance

        if target_coord > stall_coords[-1]:
            return False

        left = coord_index
        right = len(stall_coords) + 1

        while right - left > 1:
            middle = (right + left) // 2

            if target_coord <= stall_coords[middle]:
                right = middle
            else:
                left = middle

        if right >= len(stall_coords) - 1 and cow != cows_count - 2:
            return False

        coord_index = right

    return True


def get_greatest_distance(stall_coords, cows_count):
    left = 0
    right = max(stall_coords) + 1

    while right - left > 1:
        middle = (right + left) // 2

        if can_be_placed(stall_coords, cows_count, middle):
            left = middle
        else:
            right = middle

    return left


def get_array_from_input():
    return [int(val) for val in input().split()]


def main():
    [stall_count, cows_count] = get_array_from_input()
    stall_coords = get_array_from_input()

    print(get_greatest_distance(stall_coords, cows_count))


main()


assert get_greatest_distance([2, 5, 7, 11, 15, 20], 3) == 9
assert get_greatest_distance([2, 5, 7, 11, 15, 20], 4) == 5
assert get_greatest_distance([1, 2, 3, 100, 1000], 3) == 99
assert get_greatest_distance([2, 124, 155, 245, 1234], 2) == 1232
assert get_greatest_distance([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == 2
assert get_greatest_distance([100, 200, 300], 2) == 200
assert get_greatest_distance([100, 101, 300, 301], 3) == 1
assert get_greatest_distance([1, 80, 350, 400, 1000000], 4) == 79
assert get_greatest_distance([1, 80, 200, 400, 1000], 4) == 199
assert get_greatest_distance([2, 124, 155, 245, 1000000], 4) == 121

# Количество стоил всегда больше 2
# Количество коров всегда меньше количества стоил