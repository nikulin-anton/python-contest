def min_stolen_keyboards(count, keyboardsNumbers):
    return max(keyboardsNumbers) - min(keyboardsNumbers) - count + 1


array_size = int(input())
array = list(map(lambda x: int(x), input().split()))
print(min_stolen_keyboards(array_size, array))

assert min_stolen_keyboards(4, [10, 13, 12, 8]) == 2
assert min_stolen_keyboards(5, [7, 5, 6, 4, 8]) == 0