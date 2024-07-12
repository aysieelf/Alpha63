def from_string(the_string, *, pair_sep=',', kv_sep='=', value_type='str'):
    """
    Parses a string into a dictionary based on specified separators and value type.

    Parameters:
        the_string (str) - The source string to be parsed.
        pair_sep (str, optional) - Pair separator (default = ',').
        kv_sep (str, optional) - Key-Value separator (default = '=')
        value_type (str, optional) - Type of the value: ('str', 'int', 'float') (default = 'str')

    Returns:
        (dict) - The parsed dictionary
    """
    parsed_dict = {}
    pairs = the_string.split(pair_sep)

    for pair in pairs:
        key, value = pair.split(kv_sep)

        if value_type == 'int':
            value = int(value)
        elif value_type == 'float':
            value = float(value)

        parsed_dict[key] = value

    return parsed_dict


def aggregate(data):
    """
    Aggregates a list of 2-tuples into a dictionary.
    Values with duplicate keys are grouped into a list.

    Parameters:
        data (list) - The list of 2-tuples

    Returns:
        (dict) - The aggregated dictionary
    """
    aggregated_dict = {}
    rev_key = []

    for tuple in data:
        if tuple[0] in rev_key:
            aggregated_dict[tuple[0]].append(tuple[1])
        else:
            aggregated_dict[tuple[0]] = [tuple[1]]
            rev_key.append(tuple[0])

    return aggregated_dict


def aggregate_min(data):
    """
    Aggregates a list of 2-tuples into a dictionary.

    Parameters:
        data (list) - the list of 2 tuples

    Returns:
        (dict) - the aggregated dictionary
    """
    result = {}

    for key, value in data:
        if key in result:
            result[key] = min(result[key], value)
        else:
            result[key] = value

    return result


def aggregate_max(data):
    """
    Aggregates a list of 2-tuples into a dictionary. The sum of values for each unique key is aggregated.

    Parameters:
        data (list) - The list of 2-tuples

    Returns:
        (dict) - The aggregated dictionary
    """
    dict_ = {}

    for key, value in data:
        if key not in dict_:
            dict_[key] = value
        else:
            dict_[key] = max(dict_[key], value)

    return dict_


def aggregate_sorted(data, *, reverse=False):
    """
    Aggregates a list of 2-tuples into a dictionary.
    The values for duplicate keys are sorted in increasing or decreasing order.

    Parameters:
        data (list) - The list of 2-tuples
        reverse (bool) - Normal or Reverse sort (default = False)

    Returns:
        (dict) - The aggregated dictionary
    """
    dict_agg = {}

    for tup in data:
        if tup[0] in dict_agg:
            dict_agg[tup[0]].append(tup[1])
        else:
            dict_agg[tup[0]] = [tup[1]]

    for key in dict_agg:
        dict_agg[key].sort(reverse=reverse)

    return dict_agg


def aggregate_avg(data):
    """
    Aggregates a list of 2-tuples into a dictionary.
    The average of values for each unique key is aggregated.

    Parameters:
        data (list): The list of 2-tuples

    Returns:
        dict: The aggregated dictionary
    """
    sum_dict = {}
    count_dict = {}

    for key, value in data:
        if key in sum_dict:
            sum_dict[key] += value
            count_dict[key] += 1
        else:
            sum_dict[key] = value
            count_dict[key] = 1

    avg_dict = {key: sum_dict[key] / count_dict[key] for key in sum_dict}

    return avg_dict


def aggregate_sum(data):
    """
    Aggregates a list of 2-tuples into a dictionary.
    The sum of values for each unique key is aggregated.

    Parameters:
        data (list) - The list of 2-tuples

    Returns:
        (dict) - The aggregated dictionary
    """
    aggregated_dict = {}

    for key, value in data:
        if key in aggregated_dict:
            aggregated_dict[key] += value
        else:
            aggregated_dict[key] = value

    return aggregated_dict


def aggregate_count(data):
    """
    Aggregates a list of 2-tuples into a dictionary.
    The count of values for each unique key is aggregated.

    Parameters:
        data (list) - The list of 2-tuples

    Returns:
        (dict) - The aggregated dictionary
    """
    aggregated_dict = {}
    rev_key = []

    for tuple in data:
        if tuple[0] in rev_key:
            aggregated_dict[tuple[0]] += 1
        else:
            aggregated_dict[tuple[0]] = 1
            rev_key.append(tuple[0])

    return aggregated_dict


def with_keys(the_dict, keyset):
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

    for k in the_dict.keys():
        if k not in keyset:
            new_dict[k] = the_dict[k]

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
    new_dict = {}

    for key in first_dict:
        if key in second_dict:
            new_dict[key] = [first_dict[key], second_dict[key]]
        else:
            new_dict[key] = [first_dict[key]]

    for key in second_dict:
        if key not in first_dict:
            new_dict[key] = [second_dict[key]]

    return new_dict


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

    for key, value in first_dict.items():
        if key in second_dict:
            new_dict[key] = second_dict[key]

    for key, value in second_dict.items():
        if key not in new_dict:
            new_dict[key] = second_dict[key]

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
    third_dict = {}

    for key in first_dict.keys():
        if key not in second_dict.keys():
            third_dict[key] = first_dict[key]

    for key in second_dict.keys():
        if key not in first_dict.keys():
            third_dict[key] = second_dict[key]

    return third_dict


def dicts_difference(first_dict, second_dict):
    """
    Returns a new dictionary from keys in the first dictionary that are not present in the second dictionary.

    Parameters:
        first_dict (dict) - The first dictionary
        second_dict (dict) - The second dictionary

    Returns:
        (dict) - The resulting dictionary
    """
    diff_dict = {}
    rev_key = []

    for el in second_dict:
        rev_key.append(el)

    for el in first_dict:
        if el in rev_key:
            continue
        else:
            diff_dict[el] = first_dict.get(el)

    return diff_dict


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
    lst = []

    for v in the_dict.values():
        for j in v:
            lst.append(j)

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
    lst_keys = sorted(the_dict)
    result = []

    for key in lst_keys:
        temp_tuple = (key, the_dict[key])
        result.append(temp_tuple)

    return result


def dict_valuesort(the_dict):
    """
    Returns a list of tuples containing the dictionary key:value pairs sorted by value.

    Parameters:
        the_dict (dict) - The source dictionary

    Returns:
        (list) - The resulting list of tuples
    """
    value_dict = the_dict.values()
    value_dict = sorted(value_dict)
    sorted_list = {}

    while len(value_dict) != 0:
        for k, v in the_dict.items():
            if len(value_dict) == 0:
                break
            if v == value_dict[0]:
                sorted_list[k] = v
                value_dict.remove(value_dict[0])

    sorted_list = [(k, v) for k, v in sorted_list.items()]

    return sorted_list
