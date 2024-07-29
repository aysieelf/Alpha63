def valid_str_len(value: str,
                  len_min: int,
                  len_max: int,
                  err_str: str):
    if (len(value) < len_min or
            len(value) > len_max):
        raise ValueError(err_str)


def valid_num_range(value,
                    min_num: int,
                    max_num: int,
                    err_str: str):
    if (value < min_num or
            value > max_num):
        raise ValueError(err_str)
