def can_get_all_weight(n, w, array):
    array = sorted(array)
    dp = [[None for _ in range(w + 1)] for _ in range(n + 1)]
    dp[0][0] = 1

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

    return "yes" if dp[-1][-1] == 1 else "no"


def get_input():
    return list(map(int, input().split()))


def main():
    [n, w] = get_input()
    array = get_input()

    print(can_get_all_weight(n, w, array))


main()

# print(can_get_all_weight(5, 20, [2, 3, 6, 10, 1]) == "yes")
# print(can_get_all_weight(3, 10, [9, 2, 6]) == "no")
# print(can_get_all_weight(1, 5968, [18]) == "no")
