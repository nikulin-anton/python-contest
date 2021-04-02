def get_variants_count(message):
    if "w" in message or "m" in message:
        return 0

    if len(message) == 1:
        return 1

    MODULO = 10 ** 9 + 7
    dp = [None] * len(message)
    dp[0] = 1
    dp[1] = 2 if message.startswith("nn") or message.startswith("uu") else 1

    for i in range(2, len(message)):
        if (message[i] == "n" or message[i] == "u") and message[i] == message[i - 1]:
            dp[i] = (dp[i - 1] + dp[i - 2]) % MODULO
        else:
            dp[i] = (dp[i - 1]) % MODULO

    return dp[-1]


def main():
    message = input()
    print(get_variants_count(message))


main()

print(get_variants_count("ouuokarinn") == 4)
print(get_variants_count("banana") == 1)
print(get_variants_count("amanda") == 0)
# print(get_variants_count("nn") == 2)
