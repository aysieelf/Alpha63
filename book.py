my_list = [1, 2, 3]

def outer():

    my_list.append(7)

    def inner():

        nonlocal_list = my_list
        def innermost():

            global my_list

            my_list = [8, 9]

            my_list.append(10)

        innermost()

        nonlocal_list.append(11)
    inner()
    my_list.append(12)

outer()

print(my_list)