stack = []

while True:
    user_input = input().split()
    command_name = user_input[0]

    if command_name == "push":
        stack.append(user_input[1])
        print("ok")

    if command_name == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print("error")

    if command_name == "back":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print("error")

    if command_name == "size":
        print(len(stack))

    if command_name == "clear":
        stack.clear()
        print("ok")

    if command_name == "exit":
        print("bye")
        break