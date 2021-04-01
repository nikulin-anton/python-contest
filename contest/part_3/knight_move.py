def get_dinamic(n, m):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                continue

            if i == 1 and j >= 2:
                dp[i][j] = dp[i - 1][j - 2]
            elif i >= 2 and j == 1:
                dp[i][j] = dp[i - 2][j - 1]
            else:
                dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2]

    return dp[n - 1][m - 1]


def get_input():
    return [int(val) for val in input().split()]


def main():
    [n, m] = get_input()

    print(get_dinamic(n, m))


main()

print(get_dinamic(4, 4) == 2)
print(get_dinamic(7, 7) == 6)
print(get_dinamic(10, 8) == 0)
