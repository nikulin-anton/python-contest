def get_wow_effect(string):
    w, wo, wow = 0, 0, 0

    for i in range(1, len(string)):
        if string[i] == string[i - 1] == "v":
            w += 1
            wow += wo
        elif string[i] == "o":
            wo += w

    return wow


def main():
    s = input()

    print(get_wow_effect(s))


# main()

print(get_wow_effect("vovovovovovov") == 0)
print(get_wow_effect("vvvovvv") == 4)
print(get_wow_effect("vvovooovovvovoovoovvvvovovvvov") == 100)
print(get_wow_effect("vvvoovvovvv") == 18)
print(get_wow_effect("vvovvvoovvovvv") == 31)