def get_hostel_index_by_number(indexes, number):
    left = 0
    right = len(indexes)

    while right - left > 1:
        middle = (right + left) // 2
        start = indexes[middle]

        if number < start:
            right = middle
        else:
            left = middle

    return left + 1


def find_hostels_and_rooms_for_letters(rooms_count, numbers):
    indexes = []
    result = []

    for index, count in enumerate(rooms_count):
        val = 0 if index == 0 else rooms_count[index - 1] + indexes[-1]
        indexes.append(val)

    for number in numbers:
        index = number - 1
        hostel_number = get_hostel_index_by_number(indexes, index)
        room_number = number - indexes[hostel_number - 1]

        result.append([hostel_number, room_number])

    return result


def get_array_from_input():
    return [int(val) for val in input().split()]


def print_results(results):
    for result in results:
        print(f"{result[0]} {result[1]}")


def main():
    [hostels_count, letters_count] = get_array_from_input()
    rooms_count = get_array_from_input()
    numbers = get_array_from_input()

    result = find_hostels_and_rooms_for_letters(rooms_count, numbers)

    print_results(result)


main()


assert find_hostels_and_rooms_for_letters([10, 15, 12], [1, 9, 12, 23, 26, 37]) == [
    [1, 1],
    [1, 9],
    [2, 2],
    [2, 13],
    [3, 1],
    [3, 12],
]