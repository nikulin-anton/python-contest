def update_cell(i, j, n, m, dp):
    sum_all = []

    if i - 2 >= 0 and j - 1 >= 0:
        sum_all.append(dp[i - 2][j - 1])

    if i - 1 >= 0 and j - 2 >= 0:
        sum_all.append(dp[i - 1][j - 2])

    if i - 2 >= 0 and j + 1 <= m - 1:
        sum_all.append(dp[i - 2][j + 1])

    if i + 1 < n and j - 2 >= 0:
        if dp[i + 1][j - 2] == 0:
            update_cell(i + 1, j - 2, n, m, dp)

        sum_all.append(dp[i + 1][j - 2])

    if len(sum_all):
        dp[i][j] = sum(sum_all)


def get_dinamic(n, m):
    if n > m:
        n, m = m, n

    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            update_cell(i, j, n, m, dp)

    return dp[n - 1][m - 1]


def get_input():
    return [int(val) for val in input().split()]


def main():
    [n, m] = get_input()

    print(get_dinamic(n, m))


main()

# print(get_dinamic(4, 4) == 2)
# print(get_dinamic(6, 6))
# print(get_dinamic(7, 15) == 13309)
