def seconds_to_time(seconds: int) -> str:
    """
    Converts seconds to time in the following format "hh:mm:ss".

    Parameters:
        seconds (int) : Seconds.

    Returns:
        output (str) : String in the following format "hh:mm:ss".
    """
    # Hours
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


# Test cases
x = seconds_to_time(3661)  # x should be "01:01:01"
print(x)
x = seconds_to_time(45)    # x should be "00:00:45"
print(x)
