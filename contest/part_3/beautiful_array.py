def get_beautiful(array, length, x):
    dp = [[0, 0, 0]]
    max_value = 0

    for i in range(length):
        normal = max(dp[-1][0] + array[i], array[i], 0)
        multiple = max(dp[-1][1] + array[i] * x, dp[-1][0] + array[i] * x)
        end_x = max(dp[-1][1] + array[i], dp[-1][2] + array[i])

        inner_max = max(normal, multiple, end_x)
        max_value = inner_max if inner_max > max_value else max_value

        dp.append([normal, multiple, end_x])

    return max_value


def get_input():
    return [int(val) for val in input().split()]


def main():
    [array_length, x] = get_input()
    array = get_input()

    print(get_beautiful(array, array_length, x))


main()


print(get_beautiful([-3, 8, -2, 1, -6], 5, -2) == 22)
print(get_beautiful([10, -5, 10, -3, -5], 5, 1) == 15)
print(get_beautiful([-200, 150, -150, 150], 4, -1) == 450)
print(get_beautiful([-200, 150, -150, 150, 200], 5, -1) == 650)
print(get_beautiful([1, 3, 3, 7, 1, 3, 3, 7, 1, 3, 3, 7], 12, -3) == 42)