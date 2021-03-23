def is_right_brackets(brackets):
    opened = ["[", "(", "{"]
    opposite = {")": "(", "}": "{", "]": "["}
    stack = []

    for bracket in brackets:
        if bracket in opened:
            stack.append(bracket)
        else:
            if len(stack) == 0 or stack.pop() != opposite.get(bracket):
                return "no"

    if len(stack) > 0:
        return "no"

    return "yes"


user_input = input()
print(is_right_brackets(user_input))


assert is_right_brackets("()[]") == "yes"
assert is_right_brackets("([)]") == "no"
assert is_right_brackets("(()[{}]{})") == "yes"
assert is_right_brackets("") == "yes"
assert is_right_brackets("()[]{}[()]()[]") == "yes"
assert is_right_brackets(")))}}}{{") == "no"
assert is_right_brackets("())") == "no"
assert is_right_brackets("[]({}[]{}(()[]){})[]{") == "no"
