in_queue = []
out_queue = []

while True:
    user_input = input().split()
    command = user_input[0]

    if command == "push":
        in_queue.append(user_input[1])
        print("ok")

    if command == "pop":
        if len(out_queue) > 0:
            print(out_queue.pop())
        else:
            for element in reversed(in_queue):
                out_queue.append(element)

            in_queue.clear()
            print(out_queue.pop())

    if command == "front":
        if len(out_queue) > 0:
            print(out_queue[-1])
        else:
            print(in_queue[0])

    if command == "size":
        print(len(in_queue) + len(out_queue))

    if command == "clear":
        in_queue.clear()
        out_queue.clear()
        print("ok")

    if command == "exit":
        print("bye")
        break
