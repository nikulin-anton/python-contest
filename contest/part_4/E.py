def get_subsequence(max_value, max_value_index, sequence, dp):
    subsequence = [sequence[max_value_index]]
    current_index = max_value_index

    while max_value > len(subsequence):
        inner_max = None
        inner_max_index = None

        for i in range(current_index - 1, -1, -1):
            if dp[i] == dp[current_index] - 1 and sequence[i] < sequence[current_index]:
                inner_max = sequence[i]
                inner_max_index = i

        subsequence.append(inner_max)
        current_index = inner_max_index

    return subsequence


def get_max_value(dp, n, sequence):
    max_value = 0
    max_value_index = None

    for i in range(n):
        if i == 0:
            dp[i] = 1
            continue

        dp[i] = 1

        for j in range(i, -1, -1):
            value = dp[j] + 1

            if j < i and sequence[j] < sequence[i] and value > dp[i]:
                dp[i] = value

                if value > max_value:
                    max_value = value
                    max_value_index = i

    return max_value, max_value_index


def get_nvp(n, sequence):
    dp = [None for _ in range(n)]
    max_value, max_value_index = get_max_value(dp, n, sequence)
    subsequence = get_subsequence(max_value, max_value_index, sequence, dp)

    return [max_value, list(reversed(subsequence))]


def get_input():
    return list(map(int, input().split()))


def main():
    [n] = get_input()
    sequence = get_input()
    result = get_nvp(n, sequence)

    print(result[0])
    print(" ".join(str(num) for num in result[1]))


main()

# print(get_nvp(6, [3, 29, 5, 5, 28, 6]) == [3, [3, 5, 28]])
# print(get_nvp(7, [6, 1, 1, 1, 2, 3, 4]) == [4, [1, 2, 3, 4]])
# print(get_nvp(9, [4, 8, 2, 6, 2, 10, 6, 29, 58, 9]) == [5, [4, 8, 10, 29, 58]])
