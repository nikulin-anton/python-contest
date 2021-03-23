stack = []
number = None


def push():
    stack.append(int(number))
    print("ok")


def pop():
    if len(stack) == 0:
        print("error")
    else:
        print(int(stack.pop()))


def back():
    if len(stack) == 0:
        print('error')
    else:
        print(stack[-1])


def size():
    print(len(stack))


def clear():
    stack.clear()
    print("ok")


def c_exit():
    print("bye")
    exit()


commands = {
    "push": push,
    "pop": pop,
    "back": back,
    "size": size,
    "clear": clear,
    "exit": c_exit
}


def run():
    command = input()
    attrs = command.split()
    command_name = attrs[0]

    if len(attrs) > 1:
        global number
        number = attrs[1]

    commands.get(command_name)()
    run()


run()
