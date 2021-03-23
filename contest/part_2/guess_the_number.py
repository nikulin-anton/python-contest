def guess_the_number():
    left = 1
    right = 1000001

    while right - left > 1:
        middle = (right + left) // 2

        print(middle, flush=True)
        answer = input()

        if answer == ">=":
            left = middle
        else:
            right = middle

    print(f"! {left}")


guess_the_number()