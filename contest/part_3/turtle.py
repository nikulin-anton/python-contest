def get_steps(n, m, dp):
    steps = []
    i = n - 1
    j = m - 1

    while i != 0 or j != 0:
        if i == 0:
            j -= 1
            steps.append("R")
            continue

        if j == 0:
            i -= 1
            steps.append("D")
            continue

        left = dp[i][j - 1]
        top = dp[i - 1][j]

        if i == 0 or left > top:
            j -= 1
            steps.append("R")
        elif j == 0 or left <= top:
            i -= 1
            steps.append("D")

    return list(reversed(steps))


def get_optimal_path(n, m, table):
    dp = []
    line = [table[0][0]]

    for i in range(1, m):
        line.append(line[i - 1] + table[0][i])

    dp.append(line)

    for i in range(1, n):
        dp.append([dp[i - 1][0] + table[i][0]])

    for i in range(1, n):
        for j in range(1, m):
            from_top = dp[i - 1][j] + table[i][j]
            from_left = dp[i][j - 1] + table[i][j]

            dp[i].append(max(from_top, from_left))

    steps = get_steps(n, m, dp)

    return [dp[n - 1][m - 1], steps]


def print_result(result):
    print(result[0])
    print(" ".join(result[1]))


def get_array_from_input():
    return [int(val) for val in input().split()]


def main():
    [n, m] = get_array_from_input()
    table = [get_array_from_input() for i in range(n)]
    result = get_optimal_path(n, m, table)

    print_result(result)


main()


assert (
    get_optimal_path(
        5,
        5,
        [
            [9, 9, 9, 9, 9],
            [3, 0, 0, 0, 0],
            [9, 9, 9, 9, 9],
            [6, 6, 6, 6, 8],
            [9, 9, 9, 9, 9],
        ],
    )
    == [74, ["D", "D", "R", "R", "R", "R", "D", "D"]]
)
