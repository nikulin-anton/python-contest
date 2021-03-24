def fibonacci(n):
    dp = [1, 1]

    for i in range(2, n):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[-1]


def main():
    num = int(input())
    print(fibonacci(num))


main()


assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(5) == 5
assert fibonacci(6) == 8