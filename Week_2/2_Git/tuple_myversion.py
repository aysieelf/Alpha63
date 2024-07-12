def split_tuple(the_tuple, splitter):
    """
    Returns a list of tuples created by splitting a larger tuple at provided splitter.

    Parameters:
        the_tuple (tuple) - The tuple to be split
        splitter (any) - Value that splits the tuple

    Returns:
        (list) - List containing the tuple parts
    """
    new_lst = []
    temp_lst = []
    for el in the_tuple:
        if el == splitter:
            new_lst.append(tuple(temp_lst))
            temp_lst = []
        else:
            temp_lst.append(el)

    if temp_lst:
        new_lst.append(tuple(temp_lst))

    return new_lst

def merge_tuples(first_tuple, second_tuple):
    """
    Returns a list of 2-tuples that is the product of the merging of two variable-length tuples.
    None is used to fill missing values in case of different lengths.

    Parameters:
        first_tuple (tuple) - The first tuple
        second_tuple (tuple) - The second tuple

    Returns:
        (list) - List containing the merge 2-tuples
    """
    max_len = max(len(first_tuple), len(second_tuple))
    new_lst = []
    for i in range(max_len):

        if i < len(first_tuple):
            first_value = first_tuple[i]
        else:
            first_value = None

        if i < len(second_tuple):
            second_value = second_tuple[i]
        else:
            second_value = None

        new_lst.append((first_value, second_value))

    return new_lst


def sum_tuples(first_tuple, second_tuple):
    """
    Returns a new tuple that is the result of the summing of two other tuples.

    Parameters:
        first_tuple (tuple) - The first tuple
        second_tuple (tuple) - The second tuple

    Returns:
        (tuple) - The resulting summed tuple
    """
    max_len = max(len(first_tuple), len(second_tuple))
    new_lst = []
    for i in range(max_len):

        if i < len(first_tuple):
            first_value = first_tuple[i]
        else:
            first_value = 0

        if i < len(second_tuple):
            second_value = second_tuple[i]
        else:
            second_value = 0

        new_lst.append((first_value, second_value))

    return tuple(new_lst)


def sum_tuple_with(the_tuple, number):
    """
    Returns a new tuple that is the result of a number added to each of another tuples values.

    Parameters:
        the_tuple (tuple) - The source tuple
        number (int) - The number to add to each tuple value

    Returns:
        (tuple) - The resulting summed tuple
    """
    new_lst = [el+number for el in the_tuple]
    return tuple(new_lst)


def contains_subtuple(sub_tuple, the_tuple):
    """
    Returns a bool indicating whether
    a smaller tuple is a subrange of a larger tuple.

    Parameters:
        sub_tuple (tuple) - The tuple to check whether it's a part of the larger tuple
        the_tuple (tuple) - The larger tuple

    Returns:
        (bool) - The result of the check
    """
    for i in range(len(the_tuple)-len(sub_tuple) + 1):
        if sub_tuple == the_tuple[i:i+len(sub_tuple)]:
            return True

    return False


def delete_subtuple(sub_tuple, the_tuple):
    """
    Returns a new tuple that is the result of a subtuple removed from a larger one.
    Returns the larger tuple if it does not contain the smaller one.

    Parameters:
        sub_tuple (tuple) - The tuple to be removed
        the_tuple (tuple) - The larger tuple

    Returns:
        (tuple) - The resulting tuple
    """
    index = -1
    for i in range(len(the_tuple)-len(sub_tuple) + 1):
        if sub_tuple == the_tuple[i:i+len(sub_tuple)]:
            index = i
    if index == -1:
        return the_tuple
    new_lst = the_tuple[:index] + the_tuple[index+len(sub_tuple):]

    return tuple(new_lst)

def subtuple_index(sub_tuple, the_tuple):
    """
    Returns the index from where a subtuple starts in a large tuple,
    or -1 if it is not contained in it.

    Parameters:
        sub_tuple (tuple) - The smaller tuple
        the_tuple (tuple) - The larger tuple

    Returns:
        (int) - The starting index
    """
    for i in range(len(the_tuple)):
        if sub_tuple == the_tuple[i:i + len(sub_tuple)]:
            return i

    return -1


def insert_subtuple(sub_tuple, the_tuple, index):
    """
    Returns a new tuple that is the result of a tuple inserted into another one at a specified index.
    Returns the second tuple, if the insertion index is invalid.

    Parameters:
        sub_tuple (tuple) - The tuple to be inserted
        the_tuple (tuple) - The tuple to insert at
        index (int) - The insertion index

    Returns:
        (tuple) - The result of the insertion.
    """
    if index >= len(the_tuple):
        return the_tuple

    if index < 0:
        index = len(the_tuple) + index
    new_lst = the_tuple[:index] + sub_tuple + the_tuple[index:]

    return new_lst


def concat_tuples(*tuples):
    """
    Returns a new tuple that is the result
    of the concatenation of zero or more other tuples.

    Parameters:
        *tuples (variable-length argument list) - The zero or more tuples to concat

    Returns:
        (tuple) - The result of the concatenation.
    """
    new_lst = [el for tup in tuples for el in tup]

    return tuple(new_lst)


def replace_subtuple(sub_tuple, new_sub_tuple, the_tuple):
    """
    Replace a subtuple in a tuple with a new subtuple.
    Returns the original tuple if it does not contain the subtuple to be replaced.

    Parameters:
        sub_tuple (tuple) - The subtuple to be replaced
        new_sub_tuple (tuple) - The new subtuple
        the_tuple (tuple) - The target tuple

    Returns:
        (tuple) - The resulting tuple
    """
    index = -1
    for i in range(len(the_tuple) - len(sub_tuple) + 1):
        if sub_tuple == the_tuple[i:i + len(sub_tuple)]:
            index = i
            break
    if index == -1:
        return the_tuple
    new_lst = the_tuple[:index] + new_sub_tuple + the_tuple[index + len(sub_tuple):]

    return tuple(new_lst)