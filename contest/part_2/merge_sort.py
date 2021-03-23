def merge_sort(array):
    length = len(array)

    if length > 2:
        part_1 = array[: length // 2]
        part_2 = array[length // 2 :]
        result = []

        sorted_part_1 = list(reversed(merge_sort(part_1)))
        sorted_part_2 = list(reversed(merge_sort(part_2)))

        while len(sorted_part_1) or len(sorted_part_2):
            if len(sorted_part_1) == 0:
                result.append(sorted_part_2.pop())
                continue

            if len(sorted_part_2) == 0:
                result.append(sorted_part_1.pop())
                continue

            if sorted_part_1[-1] < sorted_part_2[-1]:
                result.append(sorted_part_1.pop())
            else:
                result.append(sorted_part_2.pop())

        return result
    else:
        if length > 1 and array[0] > array[1]:
            array[0], array[1] = array[1], array[0]

        return array


array_length = input()
array = list(int(el) for el in input().split())

sorted_array = merge_sort(array)
result = " ".join(str(el) for el in sorted_array)

print(result)


# assert merge_sort([6, 7, 4, 11, 6, 8]) == [4, 6, 6, 7, 8, 11]
# assert merge_sort([4, 12, 4, 1, 6, 5, 123, 9]) == [1, 4, 4, 5, 6, 9, 12, 123]