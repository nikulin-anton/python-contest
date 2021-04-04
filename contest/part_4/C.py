def find_index(unsorted, item, indexes, start=0):
    index = unsorted.index(item, start)
    value = index + 1

    if value in indexes:
        return find_index(unsorted, item, indexes, value)
    else:
        return value


def get_indexes(unsorted, items):
    start = 0
    indexes = []

    for item in items:
        indexes.append(find_index(unsorted, item, indexes, start))

    return sorted(indexes, reverse=True)


def get_items_from_cords(dp, array, max_cords, max_value):
    items = []
    [i, j] = max_cords

    while max_value > 0:
        prev_value = dp[i - 1][j]
        next_value = dp[i - 1][j - array[i - 1][0]] + array[i - 1][1]

        if prev_value > next_value:
            i -= 1
        else:
            items.append(array[i - 1])
            max_value -= array[i - 1][1]
            j = j - array[i - 1][0]
            i -= 1

    return items


def get_max_values(n, w, array, dp):
    INF = float("inf")
    max_value = 0
    max_cords = [0, 0]

    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 and j == 0:
                continue

            if i == 0:
                dp[i][j] = -INF
                continue

            if i - 1 >= 0 and j - array[i - 1][0] >= 0:
                prev_value = dp[i - 1][j]
                new_value = dp[i - 1][j - array[i - 1][0]] + array[i - 1][1]
                dp[i][j] = max(prev_value, new_value)
            else:
                dp[i][j] = dp[i - 1][j]

            if dp[i][j] > max_value:
                max_value = dp[i][j]
                max_cords = [i, j]

    return max_value, max_cords


def get_max_cost(n, w, weights, prices):
    unsorted = [[weights[i], prices[i]] for i in range(n)]
    array = sorted(unsorted, key=lambda x: x[0])

    dp = [[None for _ in range(w + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    max_value, max_cords = get_max_values(n, w, array, dp)
    items = get_items_from_cords(dp, array, max_cords, max_value)
    indexes = get_indexes(unsorted, items)

    return [len(indexes), indexes]


def get_input():
    return list(map(int, input().split()))


def main():
    [n, w] = get_input()
    weights = get_input()
    prices = get_input()

    result = get_max_cost(n, w, weights, prices)

    print(result[0])
    print(" ".join(str(num) for num in result[1]))


main()

print(get_max_cost(4, 6, [2, 4, 1, 2], [7, 2, 5, 1]) == [3, [4, 3, 1]])
print(get_max_cost(3, 10, [1, 2, 9], [5, 11, 3]) == [2, [2, 1]])
print(get_max_cost(2, 10, [10, 9], [100, 80]) == [1, [1]])
print(get_max_cost(5, 10, [8, 5, 5, 5, 5], [100, 55, 55, 55, 55]) == [2, [3, 2]])
