def try_parse_float(float_string: str, msg: str):
    try:
        return float(float_string)
    except:
        raise ValueError(msg)
