def try_parse_float(float_string: str, msg: str):
    try:
        return float(float_string)
    except:
        raise ValueError(msg)


def valid_str_len(value: str,
                  min_num: int,
                  max_num: int,
                  err: str) -> str:

    if len(value) < min_num or len(value) > max_num:
        raise ValueError(err)

    return value


def validate_params_count(params, class_name, count):
    if len(params) != count:
        raise ValueError(
            f'{class_name[:-7]} command expecte {count} parameters.')

    return params
