def sort(array):
    for index, value in enumerate(array):
        unsorted_array = array[index : len(array)]
        min_value = value
        min_value_index = index

        for inner_index, inner_value in enumerate(unsorted_array):
            if inner_value < min_value:
                min_value = inner_value
                min_value_index = inner_index + index

        array[index], array[min_value_index] = min_value, value

    return array


arr_size = input()
array = list(map(lambda value: int(value), input().split()))
print(" ".join(str(value) for value in (sort(array))))


assert sort([1, 45, 12, 3, 5]) == [1, 3, 5, 12, 45]
assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]