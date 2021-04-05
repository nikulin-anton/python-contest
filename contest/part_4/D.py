def get_max_length(array_n, array_m):
    len_n = len(array_n)
    len_m = len(array_m)
    dp = [[None for _ in range(len_m + 1)] for _ in range(len_n + 1)]
    dp[0][0] = 0

    for i in range(len_n + 1):
        for j in range(len_m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue

            values = [dp[i - 1][j], dp[i][j - 1]]

            if array_n[i - 1] == array_m[j - 1]:
                values.append(dp[i - 1][j - 1] + 1)

            dp[i][j] = max(values)

    return dp[-1][-1]


def get_input():
    return list(map(int, input().split()))


def main():
    [length_n] = get_input()
    array_n = get_input()
    [length_m] = get_input()
    array_m = get_input()

    print(get_max_length(array_n, array_m))


main()

# print(get_max_length([1, 2, 3], [2, 1, 3, 5]) == 2)
# print(get_max_length([1, 2, 3], [1001, 1002, 1003]) == 0)
