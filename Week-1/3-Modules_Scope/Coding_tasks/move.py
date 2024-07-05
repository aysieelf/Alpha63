index = int(input())

arr = [int(num) for num in input().split(',')]

def move(index, times, steps, command):
    for i in range(times):
        index += steps
        index = (index % len(arr) + len(arr)) % len(arr)
        # if index > len(arr) - 1:
        #     index %= len(arr)
        # while index < 0:
        #     index += len(arr)
        if command == "forward":
            forward_sum.append(arr[index])
        elif command == "backwards":
            backwards_sum.append(arr[index])
    return index


forward_sum = []
backwards_sum = []

while True:
    cmd = input()
    if cmd == "exit":
        break
    times, command, steps = cmd.split()
    times, steps = int(times), int(steps)
    if command == "backwards":
        steps *= (-1)
    index = move(index, times, steps, command)


print(f'''Forward: {sum(forward_sum)}
Backwards: {sum(backwards_sum)}''')
