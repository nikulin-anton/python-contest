def insertion_sort(array):
    for index, value in enumerate(array):
        sorted_array = array[0:index]
        current_index = index

        for i in range(index, 0, -1):
            sorted_index = i - 1
            sorted_value = sorted_array[sorted_index]

            if value < sorted_value:
                array[sorted_index] = value
                array[current_index] = sorted_value
                current_index = sorted_index

    return array


array_size = input()
array = list(map(lambda x: int(x), input().split()))
sorted_array = insertion_sort(array)
print(" ".join(str(num) for num in sorted_array))


assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert insertion_sort([1, 34, 56, 3, 2, 1]) == [1, 1, 2, 3, 34, 56]
