def validate_params_count(params: list[str], count: int) -> None:
    if len(params) != count:
        raise ValueError(
            f"Command needs {count} arguments, received {len(params)} instead")


def try_parse_int(value):
    if isinstance(value, int):
        return value
    elif isinstance(value, str) and value.isdigit():
        return int(value)
    raise ValueError('Invalid value - should be a number.')
