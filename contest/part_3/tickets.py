def get_fastest(customers_count, all_time):
    dp = [0, all_time[0][0], all_time[0][1], all_time[0][2]]

    for i in range(1, customers_count):
        for j in range(3):
            num = i + j + 1
            val = dp[num - (j + 1)] + all_time[i][j]

            if num >= len(dp):
                dp.append(val)
            else:
                dp[num] = min(dp[num], val)

    return dp[customers_count]


def get_array_from_input():
    return [int(num) for num in input().split()]


def main():
    [customers_count] = get_array_from_input()
    all_time = [get_array_from_input() for _ in range(customers_count)]
    result = get_fastest(customers_count, all_time)

    print(result)


main()

# print(
#     get_fastest(5, [[5, 10, 15], [2, 10, 15], [5, 5, 5], [20, 20, 1], [20, 1, 1]]) == 12
# )

# print(get_fastest(3, [[4, 4, 4], [5, 5, 5], [6, 6, 6]]) == 4)
# print(get_fastest(4, [[4, 4, 4], [1, 5, 5], [1, 6, 6], [1, 6, 6]]) == 5)
