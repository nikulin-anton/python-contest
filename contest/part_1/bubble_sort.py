def bubble_sort(array):
    unchanged = False

    while unchanged == False:
        unchanged = True

        for index, value in enumerate(array):
            if index == 0:
                continue

            prev_value = array[index - 1]

            if value < prev_value:
                array[index - 1] = value
                array[index] = prev_value
                unchanged = False

    return array


array_size = input()
array = list(map(lambda x: int(x), input().split()))
sorted_array = bubble_sort(array)
print(" ".join(str(num) for num in sorted_array))


assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert bubble_sort([1, 34, 56, 3, 2, 1]) == [1, 1, 2, 3, 34, 56]