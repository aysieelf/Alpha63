def append(list):
    list.append(1)

list = [0]
append(list)
print(list)


def reassign(list):
    list = [0, 1]

list = [0]
reassign(list)
print(list)