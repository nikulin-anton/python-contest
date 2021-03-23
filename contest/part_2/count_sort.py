def count_sort(array):
    min_num = None
    max_num = None

    for num in array:
        if min_num is None or num < min_num:
            min_num = num
        if max_num is None or num > max_num:
            max_num = num

    offset = 0 if min_num > 0 else -min_num
    count_array = [0] * (max_num + offset + 1)
    sorted_array = []

    for num in array:
        result_num = num + offset
        count_array[result_num] += 1

    for index, value in enumerate(count_array):
        result_num = index - offset

        for num in range(value):
            sorted_array.append(result_num)

    return sorted_array


array_length = input()
array = list(int(el) for el in input().split())

sorted_array = count_sort(array)
result = " ".join(str(el) for el in sorted_array)

print(result)

# assert count_sort([6, 7, 4, 11, 6, 8]) == [4, 6, 6, 7, 8, 11]
# assert count_sort([4, 12, 4, 1, 6, 5, 123, 9]) == [1, 4, 4, 5, 6, 9, 12, 123]
# assert count_sort([12, 12, 5, 6, 1, -12, -4, 66]) == [-12, -4, 1, 5, 6, 12, 12, 66]