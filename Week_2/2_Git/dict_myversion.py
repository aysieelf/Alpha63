def from_string(the_string: str, *, pair_sep: str = ',', kv_sep: str = '=', value_type: str = 'str') -> dict[str, any]:
    """
    Parses a dictionary from a string.

    Parameters:
        the_string (str): The source string
        pair_sep (str): Pair separator (default = ',')
        kv_sep (str): Key-Value separator (default = '=')
        value_type (str): Type of the value:('str', 'int', 'float') (default = 'str')

    Returns:
        (dict): The parsed dictionary

    Raises:
        ValueError: If the string cannot be parsed into key-value pairs.
        TypeError: If the value_type is not supported.

    """
    allowed_value_types = {'str', 'int', 'float'}
    parsed_dict = {}

    if the_string == '':
        return parsed_dict
    elif the_string[0] == '=' or the_string[-1] == '=':
        raise ValueError("Each string should contain key-value pairs.")

    pairs = the_string.split(pair_sep)

    if kv_sep == '':
        raise ValueError("Each pair must contain a key and a value separated by kv_sep.")
    if value_type not in allowed_value_types:
        raise TypeError("Supported types are 'str', 'int' and 'float'.")

    for pair in pairs:
        try:
            key, value = pair.split(kv_sep)
        except ValueError:
            raise ValueError(f"Invalid pair {pair}")

        if value_type == 'int':
            value = int(value)
        elif value_type == 'float':
            value = float(value)

        parsed_dict[key] = value

    return parsed_dict


def aggregate(data: list[tuple[any, any]]) -> dict[any, list[any]]:
    """
    Aggregates a list of 2-tuples into a dictionary. Values with duplicate keys are grouped into a list.

    Parameters:
        data (list[tuple[any, any]]): The list of 2-tuples

    Returns:
        (dict[any, list[any]]): The aggregated dictionary
    """
    aggregated_dict = {}

    for pair in data:
        try:
            key, value = pair
        except ValueError:
            raise ValueError("Each pair should contain 2 items.")

        if key in aggregated_dict:
            aggregated_dict[key].append(value)
        else:
            aggregated_dict[key] = [value]

    return aggregated_dict


def aggregate_min(data: list[tuple[any, int]]) -> dict[any, int]:
    """
    Aggregates a list of 2-tuples into a dictionary.
    The minimal of values with duplicate keys is assigned for each unique key.

    Parameters:
        data (list[tuple[any, any]]): The list of 2-tuples

    Returns:
        (dict[any, int]): The aggregated dictionary

    Raises:
        ValueError: If the pair doesn't contain two items.
        TypeError: If the value is not int.
    """
    aggregated_dict = {}

    for pair in data:
        if len(pair) != 2:
            raise ValueError("Each pair should contain 2 items.")

        key, value = pair

        if not isinstance(value, int):
            raise TypeError(f"Values must be integers. Invalid value: {value}")

        if key in aggregated_dict:
            aggregated_dict[key] = min(aggregated_dict[key], value)
        else:
            aggregated_dict[key] = value

    return aggregated_dict


def aggregate_max(data: list[tuple[any, int]]) -> dict[any, int]:
    """
    Aggregates a list of 2-tuples into a dictionary.
    The maximum of values with duplicate keys is assigned for each unique key.

    Parameters:
        data (list[tuple[any, any]]): The list of 2-tuples

    Returns:
        (dict[any, int]): The aggregated dictionary

    Raises:
        ValueError: If the pair doesn't contain two items.
        TypeError: If the value is not int.
    """
    aggregated_dict = {}

    for pair in data:
        if len(pair) != 2:
            raise ValueError("Each pair should contain 2 items.")

        key, value = pair

        if not isinstance(value, int):
            raise TypeError(f"Values must be integers. Invalid value: {value}")

        if key in aggregated_dict:
            aggregated_dict[key] = max(aggregated_dict[key], value)
        else:
            aggregated_dict[key] = value

    return aggregated_dict


def aggregate_sorted(data: list[tuple[any, int]], *, reverse: bool = False) -> dict[any, list[int]]:
    """
    Aggregates a list of 2-tuples into a dictionary.
    The values for duplicate keys are sorted in increasing or decreasing order.

    Parameters:
        data (list) - The list of 2-tuples
        reverse (bool) - Normal or Reverse sort (default = False)

    Returns:
        (dict) - The aggregated dictionary

    Raises:
        ValueError: If any pair does not contain exactly 2 items.
        TypeError: If any value is not an integer.
    """
    aggregated_dict = {}

    for pair in data:
        if len(pair) != 2:
            raise ValueError("Each pair should contain 2 items.")

        key, value = pair

        if not isinstance(value, int):
            raise TypeError(f"Values must be integers. Invalid value: {value}")

        if key in aggregated_dict:
            aggregated_dict[key].append(value)
        else:
            aggregated_dict[key] = [value]

    for key in aggregated_dict:
        aggregated_dict[key].sort(reverse=reverse)

    return aggregated_dict


def aggregate_avg(data: list) -> dict:
    """
    Aggregates a list of 2-tuples into a dictionary.
    The average of values for each unique key is aggregated.

    Parameters:
        data (list): The list of 2-tuples

    Returns:
        dict: The aggregated dictionary
    Raises:
        ValueError: If any pair does not contain exactly 2 items.
        TypeError: If any value is not an integer.
    """
    sum_dict = {}
    count_dict = {}

    for pair in data:
        if len(pair) != 2:
            raise ValueError("Each pair should contain 2 items.")

        key, value = pair

        if not isinstance(value, int):
            raise TypeError(f"Values must be integers. Invalid value: {value}")

        if key in sum_dict:
            sum_dict[key] += value
            count_dict[key] += 1
        else:
            sum_dict[key] = value
            count_dict[key] = 1

    aggregated_dict = {key: (sum_dict[key] / count_dict[key]) for key in sum_dict}

    return aggregated_dict


def aggregate_sum(data: list) -> dict:
    """
    Aggregates a list of 2-tuples into a dictionary.
    The sum of values for each unique key is aggregated.

    Parameters:
        data (list) - The list of 2-tuples

    Returns:
        (dict) - The aggregated dictionary
    """
    aggregated_dict = {}

    for pair in data:
        if len(pair) != 2:
            raise ValueError("Each pair should contain 2 items.")

        key, value = pair

        if not isinstance(value, int):
            raise TypeError(f"Values must be integers. Invalid value: {value}")

        if key in aggregated_dict:
            aggregated_dict[key] += value
        else:
            aggregated_dict[key] = value

    return aggregated_dict


def aggregate_count(data: list) -> dict:
    """
    Aggregates a list of 2-tuples into a dictionary.
    The count of values for each unique key is aggregated.

    Parameters:
        data (list) - The list of 2-tuples

    Returns:
        (dict) - The aggregated dictionary
    """
    aggregated_dict = {}

    for pair in data:
        if len(pair) != 2:
            raise ValueError("Each pair should contain 2 items.")

        key, value = pair

        if key in aggregated_dict:
            aggregated_dict[key] += 1
        else:
            aggregated_dict[key] = 1

    return aggregated_dict


def with_keys(the_dict: dict, keyset: set) -> dict:
    """
    Returns a new dictionary consisting only of the keys specified in the keyset.

    Parameters:
        the_dict (dict) - The source dictionary
        keyset (set) - The set of keys

    Returns:
        (dict) - the resulting dict
    """
    new_dict = {}

    for key in keyset:
        if key in the_dict:
            new_dict[key] = the_dict[key]

    return new_dict


def exclude_keys(the_dict, keyset):
    """
    Returns a new dictionary consisting only of the keys NOT specified in the keyset.

    Parameters:
        the_dict (dict) - The source dictionary
        keyset (set) - The set of keys

    Returns:
        (dict) - The resulting dictionary
    """
    new_dict = {}

    for key in the_dict.keys():
        if key not in keyset:
            new_dict[key] = the_dict[key]

    return new_dict


def dicts_union_preserve(first_dict, second_dict):
    """
    Returns a new dictionary where for duplicate keys,
    values are preserved in a list. (If no duplicate keys
    the value in the new dict has to be in a list also.)

    Parameters:
        first_dict (dict) - The first dictionary
        second_dict (dict) - The second dictionary

    Returns:
        (dict) - The resulting dictionary
    """
    third_dict = {}

    for key in first_dict.keys():
        if key in second_dict:
            third_dict[key] = [first_dict[key], second_dict[key]]
        else:
            third_dict[key] = [first_dict[key]]

    for key in second_dict.keys():
        if key not in third_dict:
            third_dict[key] = [second_dict[key]]

    return third_dict


def dicts_union_override(first_dict, second_dict):
    """
    Returns a new dictionary where for duplicate keys, the second value override the first value.

    Parameters:
        first_dict (dict) - The first dictionary
        second_dict (dict) - The second dictionary

    Returns:
        (dict) - The resulting dictionary
    """
    new_dict = first_dict.copy()
    new_dict.update(second_dict)

    return new_dict


def dicts_symmetric_difference(first_dict, second_dict):
    """
    Returns a new dictionary where duplicate keys are excluded.

    Parameters:
        first_dict (dict) - The first dictionary
        second_dict (dict) - The second dictionary

    Returns:
        (dict) - The resulting dictionary with the unique keys
    """
    new_dict = {key: first_dict[key] for key in first_dict if key not in second_dict}
    new_dict.update({key: second_dict[key] for key in second_dict if key not in first_dict})

    return new_dict


def dicts_difference(first_dict, second_dict):
    """
    Returns a new dictionary from keys in the first dictionary that are not present in the second dictionary.

    Parameters:
        first_dict (dict) - The first dictionary
        second_dict (dict) - The second dictionary

    Returns:
        (dict) - The resulting dictionary
    """
    new_dict = {key: first_dict[key] for key in first_dict if key not in second_dict}

    return new_dict


def dicts_intersection(first_dict, second_dict):
    """
    Returns a new dictionary from duplicate keys in both dictionaries where values are preserved in a list.

    Parameters:
         first_dict (dict) - The first dictionary
         second_dict (dict) - The second dictionary

    Returns:
        (dict) - The resulting dictionary
    """
    new_dict = {}

    for key in first_dict:
        if key in second_dict:
            new_dict[key] = [first_dict[key], second_dict[key]]

    return new_dict


def dict_flatten(the_dict):
    """
    Returns a list containing all the values from a dictionary where the values are also list.

    Parameters:
        the_dict (dict) - The dictionary where values are lists

    Returns:
        (list) - The resulting list
    """
    lst = [el for key in the_dict for el in the_dict[key]]
    return lst


def dict_keysort(the_dict):
    """
    Returns a list of tuples containing
    the dictionary key:value pairs sorted by key.

    Parameters:
        the_dict (dict) - The source dictionary

    Returns:
        (list) - The resulting list of tuples
    """
    new_dict = the_dict.copy()
    lst = [(key, value) for key, value in new_dict.items()]
    lst.sort(key=lambda x: x[0])
    return lst


def dict_valuesort(the_dict):
    """
    Returns a list of tuples containing the dictionary key:value pairs sorted by value.

    Parameters:
        the_dict (dict) - The source dictionary

    Returns:
        (list) - The resulting list of tuples
    """
    new_dict = the_dict.copy()
    lst = [(key, value) for key, value in new_dict.items()]
    lst.sort(key=lambda x: x[1])
    return lst