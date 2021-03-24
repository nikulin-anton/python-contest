def sequence_length(n):
    LIMIT = 3
    dp = [2, 4, 7]

    for i in range(LIMIT, n):
        val = 0

        for j in range(1, LIMIT + 1):
            val += dp[i - j]

        dp.append(val)

    return dp[n - 1]


def main():
    n = int(input())
    print(sequence_length(n))


main()


print(sequence_length(3))
print(sequence_length(4))
print(sequence_length(10))
