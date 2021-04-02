def get_sum(count, cords):
    cords = sorted(cords)
    dp = [0]
    dp.append(cords[1] - cords[0])

    for i in range(2, count):
        if i == 2:
            dp.append(dp[1] + (cords[2] - cords[1]))
        else:
            dp.append((cords[i] - cords[i - 1]) + min(dp[i - 2], dp[i - 1]))

    return dp[-1]


def get_input():
    return [int(val) for val in input().split()]


def main():
    [count] = get_input()
    cords = get_input()

    print(get_sum(count, cords))


main()

# print(get_sum(6, [3, 4, 6, 12, 13, 14]) == 5)
# print(get_sum(7, [6, 3, 7, 10, 15, 20, 21]) == 10)
