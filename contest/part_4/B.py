def get_max_weight(n, w, array):
    array = sorted(array)
    dp = [[None for _ in range(w + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    max_value = 0

    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 and j == 0:
                continue

            if i == 0 and j >= 0:
                dp[i][j] = 0
                continue

            if j == i:
                dp[i][j] = 1

            if i - 1 >= 0:
                if j - array[i - 1] >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - array[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

                if dp[i][j] == 1:
                    max_value = j

    return max_value


def get_input():
    return list(map(int, input().split()))


def main():
    [n, w] = get_input()
    array = get_input()

    print(get_max_weight(n, w, array))


main()

# print(get_max_weight(3, 10, [2, 5, 2]) == 9)
# print(get_max_weight(2, 3195, [38, 41]) == 79)